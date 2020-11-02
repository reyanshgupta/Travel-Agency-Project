import mysql.connector
from mysql.connector.cursor import MySQLCursor
#connect to database
mydb = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password= "",
    database ="travel"
)
mycursor = mydb.cursor()
choice = input(("Do you have a budget for the Travel? (y/n): "))
if choice == 'y' or choice == 'Y':
    budget = int(input("Enter your budget (INR): "))
    print("Packages in your budget are: ")
    sql=("SELECT * FROM package_info WHERE package_price < %s")
    mycursor.execute(sql,(budget,))
    record = mycursor.fetchall()
    for x in record:
        print(x)
    package_choice = input("Enter the number of the package you want: ")
    sql1 = ("INSERT INTO customer_info VALUES(%s,%s,%s,%s)")
    values1 = (username,package_id,no_of_people,price)
    mycursor.execute(sql1,values1)

elif choice == 'n' or choice == 'N':
    print("Available Packages are: ")
    mycursor.execute("SELECT * FROM package_info")
    record = mycursor.fetchall()
    for x in record:
        print(x)
    package_choice = input("Enter the number of the package you want: ")
    sql1 = ("INSERT INTO customer_info VALUES(%s,%s,%s,%s)")
    values1 = (username,package_id,no_of_people,price)
    mycursor.execute(sql1,values1)
else: 
    print('Wrong Choice')