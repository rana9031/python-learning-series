#Dictionary in python

info={
    "key":"value",
    "name":"rahul",
    "learning":"coding",
    "age":35,
    "is_adult":True,
    "marks":95.6
}
print(info) # {'key': 'value', 'name': 'rahul', 'learning': 'coding', 'age': 35, 'is_adult': True, 'marks': 95.6}

info={
    "name":"rahul",
    "subject":["python","c","java"],
    "topic":("dict","set"),
    "age":35,
    "is_adult":True,
    "marks":95.5
}
print(info) #{'name': 'rahul', 'subject': ['python', 'c', 'java'], 'topic': ('dict', 'set'), 'age': 35, 'is_adult': True,
print(type(info))


info={
    "name":"rahul",
    "subject":["python","c","java"],
    "topic":("dict","set"),
    "age":35,
}
print(info["name"])
print(info["subject"])
print(info["topic"])
print(info["age"])


info={
    "name":"rahul",
    "subject":["python","c","java"],
    "topic":("dict","set"),
    "age":35,
}
info["name"]="ram"
print(info["name"])
print(info["subject"])
print(info["topic"])
print(info["age"])


null_dict={}
null_dict["name"]="vivek"
print(null_dict)


# nested dictionaries:-
student={
    "name":"rahul",
    "subject":{
        "phy":98,
        "chem":97,
        "math":95
    }
}
print(student) #{'name': 'rahul', 'subject': {'phy': 98, 'chem': 97, 'math': 95}}
print(student["subject"]) # {'phy': 98, 'chem': 97, 'math': 95}
print(student["subject"]["chem"]) # 97