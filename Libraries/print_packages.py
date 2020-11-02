def print_packages():
    mycursor.execute("SELECT * FROM package_info")
    record = mycursor.fetchall()
    for x in record:
        print(x)