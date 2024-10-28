import mysql.connector as sql

password = str(input("Enter database password: "))
while password != "123":
    print("Wrong Password")
    password = str(input("Enter database password: "))

con = sql.connect(
    host="localhost",
    user="root",
    password="P3rs0nal@123"
)

cur = con.cursor()

cur.execute("SHOW DATABASES")
d = cur.fetchall()
l = [i[0] for i in d]

if "resturent" in l:
    cur.execute("USE resturent")
    print("Using Database resturent")
else:
    cur.execute("CREATE DATABASE resturent")
    cur.execute("USE resturent")
    
    qr1 = "CREATE TABLE Dish(DishName VARCHAR(20), Cost INTEGER, Cook VARCHAR(50), DishID VARCHAR(20))"
    cur.execute(qr1)
    
    qr2 = "CREATE TABLE Orders(DishIDs VARCHAR(100), Cost INTEGER, Date VARCHAR(20), Customer VARCHAR(50), PhoneNo VARCHAR(20))"
    cur.execute(qr2)
    
    qr3 = "CREATE TABLE Cook(Name VARCHAR(100), PhoneNo VARCHAR(20), Dishes VARCHAR(100), Salary INTEGER, DOB VARCHAR(20))"
    cur.execute(qr3)
    
    qr4 = "CREATE TABLE Salary(Name VARCHAR(100), PhoneNo VARCHAR(20), Bank VARCHAR(20), Month VARCHAR(20), Salary INTEGER, Days INTEGER, Net FLOAT(10, 2))"
    cur.execute(qr4)
    
    qr5 = "CREATE TABLE Expenditure(Sl_no INTEGER, Type VARCHAR(100), Cost INTEGER, Date VARCHAR(20))"
    cur.execute(qr5)
    
    con.commit()
    print("\n------------------------->>>>>>>>>>>>>Welcome<<<<<<<<<<<<<-----------------------------\n")


def dish():
    choice = input("1. Add 2. Remove 3. Display 4. Main Menu: ")
    if choice == '1':
        dn = input("Dish Name: ")
        dc = input("Dish Cost: ")
        print("\n")
        cname()
        print("\n")
        k = input("1. Hire A cook 2. Choose From Hired Cooks: ")
        
        while k not in ['1', '2']:
            print("CHOOSE A VALID OPTION!!!")
            k = input("1. Hire A cook 2. Choose From Hired Cooks: ")
        
        if k == '1':
            cook() 
        elif k == '2':
            cb = input("Cooked by: ")
            did = str(dishID()) 

            print(dn, "-", dc, "-", cb, "-", did)
            t = input("Are you sure you want to Add this Dish? Y/N: ")
            
            while t not in ['y', 'Y', 'N', 'n']:
                t = input("Choose a Valid Option - Y/N: ")
            
            if t in ['y', 'Y']:
                data = (dn, dc, cb, did)
                sql_query = "INSERT INTO Dish VALUES (%s, %s, %s, %s)"
                cur.execute(sql_query, data)
                con.commit()
                print("Data Entry Successful!")
            else:
                print("Operation Cancelled")
            dish()


    elif choice == '2':
        cur.execute("SELECT * FROM Dish")
        dishes = cur.fetchall()

        if not dishes:
            print("There are no Dishes")
            dish()
        else:
            print("Available Dishes:")
            for dish_item in dishes:
                print(f"{dish_item[0]} - {dish_item[1]} - {dish_item[2]} - {dish_item[3]}")

            did = input("Dish ID to Remove: ")
            data = (did,)

            cur.execute("SELECT * FROM Dish WHERE DishID = %s", data)
            dish_to_remove = cur.fetchall()

            if dish_to_remove:
                for item in dish_to_remove:
                    print(f"{item[0]} - {item[1]} - {item[2]} - {item[3]}")

                t = input("Are you sure you want to remove this dish? Y/N: ")
                valid_responses = ["y", "Y", "N", 'n']

                while t not in valid_responses:
                    t = input("Choose a Valid Option - Y/N: ")

                if t in ['y', 'Y']:
                    sql_query = "DELETE FROM Dish WHERE DishID = %s"
                    cur.execute(sql_query, data)
                    con.commit()
                    print("Dish removed successfully!")
                else:
                    print("Operation Cancelled")
            else:
                print("Dish not found.")

    elif choice == '3':
      cur = con.cursor()
      cur.execute("SELECT * FROM Dish")
      dishes = cur.fetchall()

      if not dishes:
          print("There are no Dishes available.")
      else:
          print("Available Dishes:")
          for dish_item in dishes:
              print(f"{dish_item[0]} - Cost: {dish_item[1]} - Cook: {dish_item[2]} - Dish ID: {dish_item[3]}")
      dish()

def cname():
    cur.execute("SELECT Name, Dishes FROM Cook")
    cooks = cur.fetchall()

    if not cooks:
        print("No Cooks Available! Please hire cooks.")
        cook() 
    else:
        print("<--- Available Cooks --->")
        for cook in cooks:
            print(f"{cook[0]} --- {cook[1]}")
def cook():
    choice = input("1. Add Cook 2. Remove Cook 3. Display Cooks 4. Main Menu: ")

    if choice == '1':
        addCook()
    elif choice == '2':
        removeCook()
    elif choice == '3':
        displayCooks()
    elif choice == '4':
        options()
    else:
        print("Select a Valid Option")
        cook()


def addCook():
    cur = con.cursor()
    
    name = input("Cook's Name: ")
    phone_no = input("Cook's Phone Number: ")
    dishes = input("Dishes Cooked: ")
    salary = int(input("Cook's Salary: "))
    dob = input("Cook's Date of Birth (YYYY-MM-DD): ")

    data = (name, phone_no, dishes, salary, dob)
    sql = "INSERT INTO Cook (Name, PhoneNo, Dishes, Salary, DOB) VALUES (%s, %s, %s, %s, %s)"
    
    cur.execute(sql, data)
    con.commit()
    print("Cook added successfully!")
    cook()


def removeCook():
    cur = con.cursor()
    cur.execute("SELECT * FROM Cook")
    cooks = cur.fetchall()

    if not cooks:
        print("No cooks available to remove.")
        cook()
    else:
        print("<--- Available Cooks --->")
        for cook_item in cooks:
            print(f"{cook_item[0]} - {cook_item[1]}") 

        name_to_remove = input("Enter Cook's Name to Remove: ")

        sql = "DELETE FROM Cook WHERE Name = %s"
        cur.execute(sql, (name_to_remove,))
        con.commit()
        print("Cook removed successfully!")
        cook() 


def displayCooks():
    cur = con.cursor()
    cur.execute("SELECT * FROM Cook")
    cooks = cur.fetchall()

    if not cooks:
        print("No cooks available!")
    else:
        print("<--- Available Cooks --->")
        for cook_item in cooks:
            print(f"Name: {cook_item[0]}, Phone: {cook_item[1]}, Dishes: {cook_item[2]}, Salary: {cook_item[3]}, DOB: {cook_item[4]}")

    cook()


def paySalary():
    cur = con.cursor()
    cur.execute("SELECT Name, PhoneNo FROM Cook")
    cooks = cur.fetchall()

    if not cooks:
        print("No cooks available to pay salary!")
        return

    print("<--- Available Cooks --->")
    for cook in cooks:
        print(f"{cook[0]} - {cook[1]}")

    name = input("Enter the name of the cook to pay salary: ")
    phone_no = input("Enter the phone number of the cook: ")

    data = (name, phone_no)
    cur.execute("SELECT * FROM Cook WHERE Name = %s AND PhoneNo = %s", data)
    cook_data = cur.fetchall()

    if not cook_data:
        print("Cook not found! Please check the name and phone number.")
        return

    month = input("Enter the month for which salary is being paid: ")
    salary = int(input("Enter the salary amount: "))
    days = int(input("Enter the number of working days: "))

    salary_data = (name, phone_no, "Bank Name", month, salary, days, net)
    sql = "INSERT INTO Salary (Name, PhoneNo, Bank, Month, Salary, Days, Net) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cur.execute(sql, salary_data)
    con.commit()
    print("Salary payment recorded successfully!")

    another = input("Do you want to pay salary for another cook? Y/N: ")
    if another.lower() == 'y':
        paySalary()


def newOrder():
    cur = con.cursor()
    cur.execute("SELECT * FROM Dish")
    dishes = cur.fetchall()

    if not dishes:
        print("No dishes available to order!")
        return

    print("<--- Available Dishes --->")
    for dish in dishes:
        print(f"{dish[3]} - {dish[0]} - {dish[1]}") 

    dish_ids = input("Enter the Dish IDs you want to order (comma-separated): ")
    dish_ids_list = [did.strip() for did in dish_ids.split(",")]

   
    total_cost = 0
    ordered_dishes = []
    for did in dish_ids_list:
        cur.execute("SELECT * FROM Dish WHERE DishID = %s", (did,))
        ordered_dish = cur.fetchall()

        if ordered_dish:
            total_cost += ordered_dish[0][1] 
            ordered_dishes.append(ordered_dish[0])
        else:
            print(f"Dish ID {did} not found!")

    if not ordered_dishes:
        print("No valid dishes were ordered!")
        return

    customer_name = input("Enter the customer's name: ")
    phone_no = input("Enter the customer's phone number: ")
    order_date = input("Enter the order date (YYYY-MM-DD): ")

    
    dish_ids_str = ",".join([dish[3] for dish in ordered_dishes])  
    order_data = (dish_ids_str, total_cost, order_date, customer_name, phone_no)

    sql = "INSERT INTO Orders (DishIDs, Cost, Date, Customer, PhoneNo) VALUES (%s, %s, %s, %s, %s)"
    cur.execute(sql, order_data)
    con.commit()
    print("Order placed successfully!")

    another = input("Do you want to place another order? Y/N: ")
    if another.lower() == 'y':
        newOrder()

def netIncome():
    cur = con.cursor()

    cur.execute("SELECT SUM(Cost) FROM Orders")
    total_income = cur.fetchone()[0] or 0 
   
    cur.execute("SELECT SUM(Cost) FROM Expenditure")
    total_expenditure = cur.fetchone()[0] or 0  
    net_income = total_income - total_expenditure

    print("\n<--- Net Income Summary --->")
    print(f"Total Income: ${total_income}")
    print(f"Total Expenditure: ${total_expenditure}")
    print(f"Net Income: ${net_income}")

    more_details = input("Do you want to see more details? Y/N: ")
    if more_details.lower() == 'y':
        viewIncomeDetails()

def viewIncomeDetails():
    cur = con.cursor()
    
    print("\n<--- Income Details --->")
    cur.execute("SELECT * FROM Orders")
    income_records = cur.fetchall()
    
    if not income_records:
        print("No income records found!")
        return

    for record in income_records:
        print(f"Order ID: {record[0]}, Dish IDs: {record[1]}, Cost: {record[2]}, Date: {record[3]}, Customer: {record[4]}, Phone: {record[5]}")

    print("\n<--- Expenditure Details --->")
    cur.execute("SELECT * FROM Expenditure")
    expenditure_records = cur.fetchall()

    if not expenditure_records:
        print("No expenditure records found!")
        return

    for record in expenditure_records:
        print(f"Sl No: {record[0]}, Type: {record[1]}, Cost: {record[2]}, Date: {record[3]}")


def expenditure():
    choice = input("1. Add Expenditure 2. Display Expenditure 3. Main Menu: ")

    if choice == '1':
        addExpenditure()
    elif choice == '2':
        displayExpenditure()
    elif choice == '3':
        options() 
    else:
        print("Select a Valid Option")
        expenditure()


def addExpenditure():
    cur = con.cursor()
    
    expenditure_type = input("Expenditure Type: ")
    cost = int(input("Expenditure Cost: "))
    date = input("Expenditure Date (YYYY-MM-DD): ")

    data = (None, expenditure_type, cost, date)  
    sql = "INSERT INTO Expenditure (Sl_no, Type, Cost, Date) VALUES (%s, %s, %s, %s)"
    
    cur.execute(sql, data)
    con.commit()
    print("Expenditure recorded successfully!")
    expenditure() 


def displayExpenditure():
    cur = con.cursor()
    cur.execute("SELECT * FROM Expenditure")
    expenditures = cur.fetchall()

    if not expenditures:
        print("No expenditure records found!")
    else:
        print("<--- Expenditure Records --->")
        for record in expenditures:
            print(f"Sl No: {record[0]}, Type: {record[1]}, Cost: {record[2]}, Date: {record[3]}")

    expenditure() 

def options():
    print("""
    1. DISHES
    2. COOKS
    3. SALARY
    4. ORDER
    5. INCOME
    6. BILLS
    """)

    while True:
        choice = input("What do you want to do? ")
        
        if choice == "1":
          dish()
        elif choice == "2":
          cook()
        elif choice == "3": 
          paySalary()
        elif choice == '4': 
          newOrder()
        elif choice == '5': 
          netIncome()
        elif choice == '6':
          expenditure()
        else:
            print("Select a Valid Option")
options()
