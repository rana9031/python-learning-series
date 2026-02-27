# 1 store the following word meanings in a python dictionary
# table:"a piece of furniture","list of fact & figures"
# cat:"a small animal"

dict={
    "table":["a piece of furniture","list of fact & figures"],
    "cat":"a small animal"
}
print(dict) #{'table': ['a piece of furniture', 'list of fact & figures'], 'cat': 'a small animal'}

# you are given a list of subjects gor students. assume one classroom is required for 1
# subject . how many classrooms are needed by all students
# "python","java","c++","python","javascirpt","java","python","java","c++","c"

subject={
    "python","java","c++","python","javascirpt","java","python","java","c++","c"
}
print(len(subject)) # 5

# 3 figure out a way to store 9 & 9.0 as separate values in the set (you can take help of 
# built in data types)

values={
    ("float",9.0),
    ("int",9)
}
print(values) # {('int', 9), ('float', 9.0)}

values={"9.0",9}
print(values) # {9, '9.0'}

# 4 wap to enter marks of 3 subjects from the user and store them in a dictionary. start
# with an empty dictionary & add one by one . use subject name as key and marks as value

marks={}
x = int(input("enter phy:"))
marks.update({"phy":x})
x = int(input("enter math:"))
marks.update({"math":x})
x = int(input("enter chem:"))
marks.update({"chem":x})
print(marks) # enter phy:10
               #enter math:20
               #enter chem:30
               #{'phy': 10, 'math': 20, 'chem': 30}



