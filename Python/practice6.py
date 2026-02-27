# let's practice
# using for

# 1 print the element of the following list using the loop

nums=[1,4,9,16,25,36,49,64,81,100]
for el in nums:
    print(el)


# 2 search for a number x in the tuple using loop


nums=(1,4,9,16,25,36,49,64,81,100,49)
x=49
idx=0
for el in nums:
    if(el==x):
        print("number found at idx",idx)
    idx+=1


nums=(1,4,9,16,25,36,49,64,81,100,49)
x=49
idx=0
for el in nums:
    if(el==x):
        print("number found at idx",idx)
        break
    idx+=1


        