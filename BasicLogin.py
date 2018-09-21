username= []
password= []

def mainmenu():
    print("\nWelcome to the entry system")
    print("Press '1' to login, press '2' to register")
    x= input()

    if(x== '1'):
        print("Your username: ")
        username_in= input()
        print("Your password: ")
        password_in= input()
        if (username_in in username and password_in in password):
            print("\nLogin successfuly")
            print("You're redirecting...")
            mainmenu()

        else:
            print("\nYour username or password incorrect!")
            print("You're redirecting...")
            mainmenu()

    if(x== '2'):
        print("Username: ")
        usernamee_in= input()
        if(usernamee_in in username):
            print("Username already exists...")
            print("You're redirecting...")
            mainmenu()

        else:
            print("Password: ")
            passwordd_in= input()
            password.append(passwordd_in)
            username.append(usernamee_in)
            print("Successful, you're redirecting to main menu")
            mainmenu()

mainmenu()

















