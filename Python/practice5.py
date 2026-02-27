# print number from 1 to 100

i=1
while i<=100:
    print(i)
    i+=1

# print number from 100 to 1

i=100
while i>=1:
    print(i)
    i-=1

# print the multiplication table of a number n

i=1
while i<=10:
    print(2*i)
    i+=1

# print the element of the following list using a loop
#[1,4,9,16,25,36,49,64,81,100]

num=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(num):
    print(num[i])
    i+=1

# search for a number x in this tuple using loop
#(1,4,9,16,25,36,49,64,81,100)

num=(1,4,9,16,25,36,49,64,81,100)
x=36
i=0
while i<len(num):
    if(num[i]==x):
        print("found at idx",i)
    else:
        print("finding:")
    i+=1