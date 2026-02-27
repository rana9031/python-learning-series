# string:-
# string is data type that stores a sequence of character

# tino tarah se likh sakte hai
str1 = "this is a string"
str2 = 'rahul kumar rana'
str3 = '''this is string'''
print(str1) # this is a string

str1 = ("this is a string. we are creating a python")
print(str1) # this is a string. we are creating a python

str1 = ("this is a string. \n we are creating a python") #\n new line mai print hoga we are creating a python
print(str1) # this is a string
            # we are creating a python


# \t a_b space aa jayega 

str1 = ("this is a string.\twe are creating a python")
print(str1) # this is a string.    we are creating a python

#concentation

str1 = "Rahul"
str2 = "Rana" 
print(str1 + str2) #RahulRana

str1 = "Ram"
str2 = "Rana"
final_str = str1 + str2
print(final_str) #RamRana

# length of str
# len(str)

str1 = "Apna"
print(len(str1)) #4 because 4 character hai

# isi ko variable banke bhi likh salte hai

str1 = "Rahul"
len1 = len(str1)
print(len1)
str2 = "Rana" 
len2 = len(str2)
print(len2)
final_str = str1 + str2 #agr final_str = str1 + " " + str2 likhte to gap aata rahulrana mai jaise rahul  rana " "(karan) ar " " karan ek length bhi badh jata 
print(len(final_str))