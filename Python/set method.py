# set methods

# 1 set.add(el)

collection=set()
collection.add(1)
collection.add(2)
collection.add(2) # ignore 
collection.add(3)
print(collection) # {1, 2, 3}

collection=set()
collection.add(1)
collection.add(2)
collection.add(2) # ignore 
collection.add(3)
collection.add("rahul") # str passing
collection.add((4,5,6)) # tuple passing / list pass nhi hota set mai
print(collection) # {1, 2, 3, 'rahul', (4, 5, 6)}

# 2 collection.remove(1) / remove the element


collection=set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.remove(1)
print(collection) # 2


# 3 set.clear()


collection=set()
collection.add(1)
collection.add(2)
collection.add(2) # ignore 
collection.add(3)
collection.clear()
print(len(collection)) # 0


# 4 set.pop() remove a random value

collection={"hello","world","apnacollege","coding","python"}
collection.pop()
print(collection) #{'hello', 'python', 'apnacollege', 'world'}

ollection={"hello","world","apnacollege","coding","python"}
collection.pop()
collection.pop()
print(collection) # {'world', 'apnacollege'}

# 5 set.union(set2)

set1={1,2,3,4,5}
set2=(5,6,7)
print(set1.union(set2)) #{1, 2, 3, 4, 5, 6, 7}

# 5 set.intersection(set2)

set1={1,2,3,4,5}
set2=(5,6,7,2,3)
print(set1.intersection(set2)) # {2, 3, 5}
