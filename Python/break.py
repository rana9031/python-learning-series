i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
print("end of loop")

num=(1,4,9,16,25,36,49,64,81,100)
x= 36
i=0
while i<=len(num):
    if(num[i]==x):
        print("found at idx",i)
        break
    else:
        print("findind")
    i+=1
print("end of loop")


# continue

i=1
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1

i=1
while i<=10:
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1

i=1
while i<=10:
    if(i%2!=0):
        i+=1
        continue
    print(i)
    i+=1

nums=[1,2,3,4,5]
for val in nums:
    print(val)

str="apnacollege"
for char in str:
    if(char=="o"):
        print("o found")
        break
    print(char)
else:
    print("END")

