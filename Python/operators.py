#arithmetic operators

a = 5
b = 2

sum = a + b
print(sum)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) #module/remainder
print(a ** b) #a^b it means a to the power b


#relational operators

a = 50
b = 20

print(a == b) #False
print(a != b) #True
print(a >= b) #True
print(a > b) #True
print(a <= b) #False
print(a < b ) #False


#Assignment operators

num = 10
num = num + 10 #/// num += 10
print(num) #20
print("num:", num) #num: 20

num = 10
num -= 10
print(num) #0

num = 10 
num *= 10
print(num) #100

num = 10
num *= 5
print(num) #50


num = 10
num /= 5
print(num) #2


num = 10
num %= 5
print(num) #0


num = 10
num **= 5
print(num) #100000



#logical operators
# 1 NOT

a = 50
b = 30
print(not False) # True
print(not(a > b)) #False


# 2 AND 
val1 = True
val2 = True
print("AND operator:", val1 and val2) #True

val1 = True
val2 = False
print("AND opertor:", val1 and val2) #False


# 3 OR operator
val1 = True
val2 = True
print("or operator:", val1 or val2) #True


val1 = True
val2 = False
print("or operator:", val1 or val2) #True


val1 = False
val2 = False
print("or operator:", val1 or val2) #False


a = 50
b = 30
print("or operator:", (a==b) or (a>b))
