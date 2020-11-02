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
mycursor.execute("SELECT * FROM user_info")
record= mycursor.fetchall()
for x in record:
    print(x)