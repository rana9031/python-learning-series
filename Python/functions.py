a=5
b=10
sum=a+b
print(sum)
# more lines of code
a=2
b=10
sum=a+b
print(sum)
# more lines of code
a=12
b=17
sum=a+b
print(sum)

# har bar code likhna pad rha hai ab isko function ke help se krege jisse har bar code n likhna 
# by functions

def cal_sum(a,b):
    sum=a+b
    print(sum)
    return sum
cal_sum(5,10)
# more lines of code
cal_sum(2,10)
# more lines of code
cal_sum(12,17)

def cal_sum(a,b):
    return a+b
sum=cal_sum(1,2)
print(sum)


def print_hello():
    print("hello")
print_hello() # hello

def print_hello():
    print("hello")
output=print_hello()
print(output) # none

# average of three number

def cal_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg
cal_avg(1,2,3) # 2.0

def cal_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg
cal_avg(98,97,95) #96.667