# Arranging three Numbers in decending order :
num1=int(input("enter the number :"))
num2=int(input("enter the number :"))
num3=int(input("enter the number :"))
number= [num1,num2,num3]
number.sort(reverse=True)
print("Numbers in decending order :", number)