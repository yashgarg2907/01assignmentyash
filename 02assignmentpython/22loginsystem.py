#Menu - Driven login system :
phone=int(input("Enter the phone number : "))
otp=int(input("Enter the otp : "))
if phone == 7610612969 and otp == 281141:
    print("Login successful with phone!")
    email=input("Enter the email : ")
    password=input("Enter the password : ")
    if email == 'sikarwarlakhan00@gmail.com' and password == 'abhinay@123':
        print("Login successful with eamil !")
        user_select=input("Enter the  option : ")
        if user_select == 'exit' :
            print("Exiting the program. Have a nice day ! ") 
            user_select=input("Enter valid option : ")
            if user_select == 'Invalid':
                print("Invalid credentials or an invalid choice : ")
            else:
                print("Appropriate error messages")
        else:
            print("Terminate the program")
    else:
        print("Invalid Login with eamil")
else:
    print("Invalid Login with phone")

