for i in range(5):
    pass
print("some work") # some work / pass lgne se uper wala kam skip ho jata hai


# practice 
# 1 wap to find the sum of digits of first natural numbers (using while)

n=7
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("total sum=",sum)

n=5
sum=0
for i in range(1,n+1):
    sum+=i
print("total sum=",sum)

# 2 wap to find the factorial of first n number (using for)

n=5
fact=1
for i in range(1,n+1):
    fact*=i
print("factorial=",fact)    

n=5
fact=1
i=1
while i<=5:
    fact*=i
    i+=1
print("factorial=",fact)