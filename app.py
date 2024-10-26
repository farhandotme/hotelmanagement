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
    print("Cook function is called. (Placeholder)")

def paySalary():
    print("PaySalary function is called. (Placeholder)")

def newOrder():
    print("NewOrder function is called. (Placeholder)")

def netIncome():
    print("NetIncome function is called. (Placeholder)")

def expenditure():
    print("Expenditure function is called. (Placeholder)")


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
