import mysql.connector as sql

password = str(input("Enter database password: "))
while password != "123":
  print("Wrong Password")
  password = str(input("Enter database password: "))


mydb = sql.connect(
  host="localhost",
  user="root",
  password="P3rs0nal@123"
)

cur = mydb.cursor()

cur.execute("show databases")
d = cur.fetchall()

l = []

for i in d:
  l.append(i[0])

if "resturent" in l:
  cur.execute("use resturent")
  print("Using Database resturent")
else:
  cur.execute("create database resturent")
  cur.execute("use resturent")
  qr1 = "create table Dish(Dish varchar(20), Cost integer, Cook varchar(50), DishID varchar(20))"
  cur.execute(qr1)
  qr2 = "create table Orders(DishIDs varcha(100), Cost integer, Date varchar(20), Costomer varchar(50), PhoneNo varchar(20))"
  cur.execute(qr2)
  qr3 = "create table Cook(Name varchar(100), PhoneNo varchar(20), Dishes varchar(100), Salary integer, DOB varchar(20))"
  cur.execute(qr3)
  qr4 = "create table Salary(Name varchar(100), PhoneNo varchar(20), Bank varchar(20), Month varchar(20), Salary integer, Days integer, Net float(10, 2))"
  cur.execute(qr4)
  qr5 = "create table Expenditure(Sl_no integer, Type varchar(100), Cost integer, Date varchar(20))"
  cur.execute(qr5)
  mydb.commit()
  print("\n")
  print("------------------------->>>>>>>>>>>>>Welcome<<<<<<<<<<<<<-----------------------------")
  print("\n")

  


