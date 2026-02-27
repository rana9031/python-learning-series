#1 waf to print the length of a list(list is the parameter)

cities=["delhi","gurgaon","noida","pune","mumbai"]
heroes=["thor","iroman","captain america","shaktiman"]

def print_len(list):
    print(len(list))
print_len(cities) # 5
print_len(heroes) # 4

#2 waf to print the element of a list in a sigle line(list is parameter)

cities=["delhi","gurgaon","noida","pune","mumbai"]
heroes=["thor","iroman","captain america","shaktiman"]

def print_list(list):
    for item in list:
        print(item,end="")
print_len(heroes)
print()

# 3 waf to find the factorial of n(n is the parameter)

n=5
fact=1
for i in range(1,n+1):
    fact*=i
print(fact) # 120

# with function

def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
cal_fact(5) # 120