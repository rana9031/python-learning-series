# conditional statements
# if-elif-else

age = 21
if(age>=18):
    print("can vote & apply for license") # can vote & apply for license

age = 20
if(age>=18):
    print("can vote") # can vote
    print("can drive") # can drive
                     

light = "green"
if(light=="red"):
    print("stop")
elif(light=="green"): # go
    print("go")
elif(light=="yellow"):
    print("look")

num = 5
if(num>2):
    print("greater than 2")  #grater than 2
    if(num>3):
        print("greater than 3") # grater than 3

#light = "pink"
#if(light=="red"):
 #   print("stop")
#elif(light=="green"):
 #   print("go")
#elif(light=="yellow"):
 #   print("look")
#else:
 #   print("light is broken") # light is broken
  #  print("end of the code") # end of the code

age = 24
if(age>=18):
    print("can vote") # can vote
else:
    print("cannot vote")

# marks = 90, grade = A
# 90> marks>= 80, grade = B
# 80> marks>= 70, grade = C
# 70> marks, grade = D

#marks = 74
#if(marks>=90):
 #   grade = "A"
#elif(marks>=80 and marks<90 ):
 #   grade = "B"
#elif(marks>=70 and marks<80): # grade = c
 #   grade = "C"
#else:
 #   grade = "D"
#print("grade of the student =",grade)
    

#marks = int(input("enter student marks :"))
#if(marks>=90):
 #   grade = "A"
#elif(marks>=80 and marks<90 ):
#    grade = "B"
#elif(marks>=70 and marks<80):
 #   grade = "C"
#else:
 #   grade = "D"
#print("grade of the student =",grade)


# nesting
age = 34
if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")
        