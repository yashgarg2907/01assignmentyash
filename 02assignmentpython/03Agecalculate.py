age=int(input("Enter the age :"))
retirement_age = 65
if retirement_age > age :
    years_left = retirement_age - age
    print(f"you have {years_left} years left until retirement")
else:
    print(f"you have already retirement age")