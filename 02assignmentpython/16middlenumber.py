# Finding the middle number ;
n1=int(input("enter the number :"))
n2=int(input("enter the number :"))
n3=int(input("enter the number :"))
if (n1 > n2 and n1 < n3) or (n1 < n3 and n1 > n2):
    print("Middle number is", n1)
elif (n2 > n3 and n2 < n1) or (n2 < n1 and n2 > n3 ):
    print("Middle number is",n2)
else: 
    print("Middle number is",n3)