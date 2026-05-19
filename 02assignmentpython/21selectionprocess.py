# Selection process :
# Task : Simulate the upsc selection process with the following steps:
age=int(input("Student Enter the age :"))
graduate=input("Student Graduate status :")
nationality=input("Student Nationality :")
if (age >=21 and age <=32 and graduate == "yes" and  nationality == "yes" ):
    print(f"Age : {age}")
    print(f"Graduate : {graduate}")
    print(f"Nationality : {nationality}")
    print("If eligible, proceed to prelims.")
    premarks=int(input("Enter the premarks :"))
    if premarks >= 600 :
        print(f"Prelims : {premarks}")
        print("If passed , proceed to mains.")
        mainsmarks=int(input("Enter the mainsmarks :"))
        if mainsmarks >= 1100:
            print(f"Mainsmarks : {mainsmarks}")
            print("If passed , proceed to interview .")
            marks=int(input("Enter the interview marks :"))
            if marks >= 1600 :
                print(f"Enterview : {marks}")
                print("If passed, Congratulation! You have cleared the UPSC")
            else:
                print("If failed , You failed the interview")
        else:
            print("If failed, you failed the mains.")
    else:
        print("If failed, you failed the prelims.")
        
else:
    print("you are out for criteria age")
    print("If ineligible , display the reason for ineligibility.")
