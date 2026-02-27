# let's practice 1
# WAP to check if a number entered by the user is odd or even

num = int(input("enter a number :"))
rem = num%2
if(rem==0): # direct if(num%2==0): 
    print("even number")
else:
   print("odd")


# WAP to find the gratest of three number entered by the user

a = int(input("enter first number :"))
b = int(input("enter second number :"))
c = int(input("enter third number :"))
if(a>=b and a>=c):
    print("A is largest number:", a)
elif(b>=c):
    print("B is the largest number:", b)
else:
    print("C is the largest number:", c)


#WAP to check if a number is multiple of 7 or not

x = int(input("enter the number:"))
if(x%7==0):
    print("multiple by 7")
else:
    print("not a multiple")    
