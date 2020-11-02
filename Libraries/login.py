
def login(username,password):
    print('Welcome to Rocket Travel Agency')

    username = input('Enter your Username: ')
    password = input('Enter password: ')
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
                            print("Welcome!")
                        else:
                            print("Wrong Password, try again")
                    break
                break
            else:    
                print('Wrong Username, try again')
        break

