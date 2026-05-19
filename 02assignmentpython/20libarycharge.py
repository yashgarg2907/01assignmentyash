# calculate library charge :
days=int(input("Enter the days a book has been borrowed :"))
if days <=5:
    charge= days * 2
    print(f"Calculate : {charge}")
elif days <= 10:
    charge = days*3
    print(f"Calculate : {charge}")
elif days <= 15:
    charge = days * 4
    print(f"Calculate : {charge}")
else:
    charge = days * 5
    print(f"Calculate : {charge}")
