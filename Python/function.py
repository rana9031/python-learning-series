# string functions
# str.endswith

str = "i am studing python from apnacollege"
print(str.endswith("ege")) #true
print(str.endswith("app"))  #false

# capitalize

str = "i am studing python from apnacollege"
print(str.capitalize())

str = "i am rahul kumar rana"
str = str.capitalize()
print(str) # I am rahul kumar rana

# replace

str = "I am a boy"
print(str.replace("a","o")) #I om o boy
print(str.replace("boy","girl")) # I am a girl

#find

str = "i am a boy"
print(str.find("o")) # 9
print(str.find("am")) #2
print(str.find("r")) #-1 because r exist hi nhi krta i am a boy mai

# count
str = "i am studing from python from apna college"
print(str.count("from")) # 2
print(str.count("o")) #4

# let's practice
# wap to input users first name and print it's length

#name = input("enter your name :")
#print("length of your name :",len(name)) #5     yesb comment out wale terminal se hoga 

# wap to find the occurence of '$' in a string

str = "hii $i am the $ symbol $99.99"
print(str.count("$")) #3