# Employees salary based on experience :
experience_emp=int(input("enter the experience :"))
if experience_emp >= 10:
    print("senior employees")
    salary = 80000
    if experience_emp > 15:
        salary = salary + 5000
        print("Experience exceeds 15 years bouns added.")
        print(f"salary : {salary}")
elif experience_emp >= 5 and experience_emp <= 9:
    print("mid-level employee")
    salary=50000
    print(f"salary : {salary}")
else:
    print("junior employee")
    salary=30000
    print(f"salary : {salary}")