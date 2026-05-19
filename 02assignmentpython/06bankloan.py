# Task: Bank loan approval system :
age=int(input("Enter the age :"))
monthly_income=int(input("Enter the monthly :"))
credit_score=int(input("Enter the credit score :"))
outstanding_debts=int(input("Enter the outstanding debts :"))
if (age >= 18 and age <= 60 and monthly_income >= 25000 and credit_score >= 700
     and outstanding_debts >= 10000):
    print(f"Age : {age}")
    print(f"Monthly income : {monthly_income}")
    print(f"Credit score : {credit_score}")
    print(f"Outstanding debts : {outstanding_debts}")
    print("Loan approved")
else:
    print("Loan rejected")
