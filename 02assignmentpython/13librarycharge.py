# Library charge calculation :
days=int(input("Enter the number of days the book has been borrowed :"))
if days  <= 5 :
    charge=days*2
    print(f"calculate : {charge}")
elif days  <= 10:
    charge = days * 3
    print(f"calculate : {charge}")
elif days  <= 15:
    charge = days * 4
    print(f"calculate : {charge}")
else:
    charge=days * 5
    print(f"calculate : {charge}")
    
 