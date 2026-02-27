# 1 list.append() add one element at the end
list=[1,2,3]
list.append(4)
print(list) # 1,2,3,4

# 2 list.sort()  sort in ascending order
list=[50,30,40,10,20]
list.sort()
print(list) # 10,20,30,40,50

list=['a','b','e','d','c']
list.sort()
print(list) #[ 'a','b','c','d','e']

list=["banana","apple","orange"]
list.sort()
print(list) # 'apple', 'banana', 'orange' because a aata h phle phr b phr...... and then o in alphabetic

list=[50,30,40,10,20]
print(list.sort()) # none
print(list) # 10,20,30,40,50

list=[50,30,40,10,20]
print(list.append(60)) #none
print(list.sort())   #none
print(list) # 10,20,30,40,50,60

# 3 list.sort(reverse=True) sort in descending order
list=[50,30,40,10,20]
list.sort(reverse=True)
print(list) # 50,40,30,20,10

# 4 list.reverse() ulta kr dega elements ko
list=[100,90,80,70,60,50,40,30,20,10]
list.reverse()
print(list) # 10,20,30,40,50,60,70,80,90,100

# 5 list.insert() insex par element ko add krna
list=[10,30]
list.insert(1,20) # 1 index par 20 aa jayega 
print(list) # 10,20,30


# 6 list.remove() remove first occurence of the element
list=[10,20,10,30,40]
list.remove(10) # pahla 10 ko remove kar dega
print(list) # 20,10,30,40


# 7 list.pop() remove element at the index
list=[10,20,30,40]
list.pop(0)
print(list) # 20,30,40

list=[1,2,3,4]
list.pop(0)
print(list) # 1,3,4