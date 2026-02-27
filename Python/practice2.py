#WAP to check if a number entered by the user is odd or even 

num=int(input("enter a number:"))
rem=num%2
if(rem==0):
    print("even number")
else:
    print("odd number")

num=int(input("enter number:"))
if(num%2==0):
    print("even") 
else:
 print("odd")


#WAP to find the greatest of 3 number entered by the user

a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if(a>=b and a>=c):
   print("a is greater:",a)
elif(b>=c and b>=c):
   print("b is greatest:",b)
else:
   print("c is greatest:",c)