# 1 my.dict.keys()

student={
    "name":"rahul",
    "subject":{
        "phy":97,
        "chem":98,
        "math":95,
    }
    }
print(student.keys()) #dict_keys(['name', 'subject'])
print(len(student)) # 2

# 2 my.dict.values()

student={
    "name":"rahul",
    "subject":{
        "phy":95,
        "chem":96,
        "math":97,
    }
}
print(student.values()) # dict_values(['rahul', {'phy': 95, 'chem': 96, 'math': 97}])
print(list(student.values())) #['rahul', {'phy': 95, 'chem': 96, 'math': 97}]

# 3 my.dict.items()


student={
    "name":"rahul",
    "subject":{
        "phy":95,
        "chem":96,
        "math":97,
    }
}
print(student.items()) #dict_items([('name', 'rahul'), ('subject', {'phy': 95, 'chem': 96, 'math': 97})])
print(list(student.items()))#[('name', 'rahul'), ('subject', {'phy': 95, 'chem': 96, 'math': 97})]

# 4 my.dict.get("keys")

student={
    "name":"rahul",
    "subject":{
        "phy":95,
        "chem":96,
        "math":97,
    }
}
print(student["name"]) # rahul
print(student.get("name")) # rahul

student={
    "name":"rahul",
    "subject":{
        "phy":95,
        "chem":96,
        "math":97,
    }
}
#print(student["name1"]) # error
print(student.get("name1")) # none

print(student["name"]) # rahul
print(student.get("name")) # rahul

student={
    "name":"rahul",
    "subject":{
        "phy":95,
        "chem":96,
        "math":97,
    }
}
print("BEFORE")
#print(student["name1"]) #
# print("AFTER") 

# 5 my.dict.update(new dict)

student={
    "name":"rahul",
    "subject":{
        "phy":95,
        "chem":96,
        "math":97,
    }
}
student.update({"city":"delhi"})
print(student) #{'name': 'rahul', 'subject': {'phy': 95, 'chem': 96, 'math': 97}, 'city': 'delhi'}

student={
    "name":"rahul",
    "subject":{
        "phy":95,
        "chem":96,
        "math":97,
    }
}
new_dict={"city":"delhi"}
student.update(new_dict)
print(student) #{'name': 'rahul', 'subject': {'phy': 95, 'chem': 96, 'math': 97}, 'city': 'deldi'}


student={
    "name":"rahul",
    "subject":{
        "phy":95,
        "chem":96,
        "math":97,
    }
}
new_dict={"city":"delhi","age":18}
student.update(new_dict)
print(student)#{'name': 'rahul', 'subject': {'phy': 95, 'chem': 96, 'math': 97}, 'city': 'delhi', 'age': 18}


student={
    "name":"rahul",
    "subject":{
        "phy":95,
        "chem":96,
        "math":97,
    }
}
new_dict={"name":"Ram"}
student.update(new_dict)
print(student)#{'name': 'Ram', 'subject': {'phy': 95, 'chem': 96, 'math': 97}}

