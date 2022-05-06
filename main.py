import mysql.connector
from mysql.connector.cursor import MySQLCursor
#connect to database
mydb = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password= "",
    database ="travel"
)
def package_choice():
    choice = input(("Do you have a budget for the Travel? (y/n): "))
    if choice == 'y' or choice == 'Y':
        budget = int(input("Enter your budget (INR): "))
        print("Packages in your budget are: \n Package name \t Price \t Package Description")
        sql=("SELECT * FROM package_info WHERE package_price < %s")
        mycursor.execute(sql,(budget,))
        record = mycursor.fetchall()
        for x in record:
            print(x)
        package_choice = input("Enter the name of the package you want: ")
        sql1 = ("INSERT INTO package_choice VALUES(%s,%s)")
        values1 = (username,package_choice)
        mycursor.execute(sql1,values1)
        print("Thank you for booking the package:",package_choice, ". We Hope to see you soon!")    
  
    elif choice == 'n' or choice == 'N':
        print("Available Packages are: ")
        mycursor.execute("SELECT * FROM package_info")
        record = mycursor.fetchall()
        for x in record:
            print(x)
        package_choice = input("Enter the name of the package you want: ")
        sql1 = ("INSERT INTO package_choice VALUES(%s,%s)")
        values1 = (username,package_choice)
        mycursor.execute(sql1,values1)
        print("Thank you for booking the package:",package_choice, ". We Hope to see you soon!")
        
    else: 
        print('Wrong Choice')
        

mycursor = mydb.cursor()
print("Welcome to Rocket Travel Agency!")
print("1. Login (already existing user)")
print("2. Register (new user)")
choice = int(input("Select your choice: "))
if choice == 1:
    username = input('Enter your Username: ')
    password = input('Enter password: ')
    user_found = 0
    mycursor.execute("SELECT user_name FROM user_info")
    record = mycursor.fetchall()
    for x in record:
        for y in x:
            if y == username: 
                mycursor.execute("SELECT user_password FROM user_info")
                record1 = mycursor.fetchall()
                for a in record1:
                    for b in a:
                        if b == password:
                            user_found = 1
                            if user_found == 1: 
                                print("Welcome ",username, "!")
                                package_choice()
                            else: 
                                break
                        elif user_found==0:
                            print("Wrong Password/Username, Please try again.")   
                            break                
                

elif choice == 2:
    print("Register-")
    mycursor = mydb.cursor()
    name = input("Enter your Name: ")
    user_name = input("Enter Username: ")
    password = input("Enter Password: ")
    sql = "INSERT INTO user_info (user_info_name,user_name,user_password) VALUES (%s,%s,%s)"
    val = (name,user_name,password)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,"Successfully Registered. ")


else:
    print("Wrong choice")      
