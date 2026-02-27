# Sets in python

collection={1,2,3,4}
print(collection) #{1, 2, 3, 4}
print(type(collection)) # <class 'set'>

collection={1,2,3,4,"hello","world"}
print(collection) # {1, 2, 3, 4, 'hello', 'world'}


collection={1,2,3,4,"hello","world","world"}
print(collection) # {1, 2, 3, 4, 'hello', 'world'}
print(len(collection)) # 6

# empty set creation

collection=set()
print(type(collection)) # <class 'set'>

