import mysql.connector
from mysql.connector.cursor import MySQLCursor
#connect to database
mydb = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password= "",
    database ="travel"
)
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
