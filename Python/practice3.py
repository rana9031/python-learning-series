#  wap to asl the user to enter name of theit favourite movies and store them in a list

movies=[]
mov1=input("enter 1st movie name:") # i
mov2=input("enter 2nd movie name:") # love
mov3=input("enter 3rd movie name:") # you

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies) #['i','love','you']


movies=[]
mov=input("enter first name:") # a
movies.append(mov)
mov=input("enter second name:") # b
movies.append(mov)
mov=input("enter third name:") # c
movies.append(mov)
print(movies) # ['a','b','c']


movies=[]
movies.append(input("enter  first name:")) # rahul
movies.append(input("enter  second name:")) # kumar
movies.append(input("enter  third name:")) # rana
print(movies) #['rahul','kumar','rana']


# wap to check if a list contain palindrome of element.(hint use copy() method)

list1=[1,2,1]
copy_list1=list1.copy()
copy_list1=reversed()
if(copy_list1==list1):
    print("palindrome")
else:
    print("not palindrome")
