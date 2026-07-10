print(1+2) # 3, aha pe add
print("apna" + "college") # apnacollege, aha pe concatenate
print([1,2,3] + [4,5,6]) #[1,2,3,4,5,6], aha +  merge form mai hai
  # + symbol same hai but sb jgah + ke alg alg form hai

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def shownumber(self):
        print(self.real,"i +",self.img,"j")

num1=Complex(1,3)
num1.shownumber() # 1i + 3j
num2=Complex(4,6)
num2.shownumber() # 4i + 6j

# ab dono complex ko add krne ka program karege

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def shownumber(self):
        print(self.real,"i +",self.img,"j")

    def add(self,num2):
        newreal=self.real + num2.real
        newimg=self.img + num2.img
        return Complex(newreal,newimg)

num1=Complex(1,3)
num1.shownumber() # 1i + 3j
num2=Complex(4,6)
num2.shownumber() # 4i + 6j
num3=num1.add(num2)
num3.shownumber()  # 5i + 9j

# ab dunder function ki madad se krege

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def shownumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2):
        newreal=self.real + num2.real
        newimg=self.img + num2.img
        return Complex(newreal,newimg)

num1=Complex(1,3)
num1.shownumber() # 1i + 3j
num2=Complex(4,6)
num2.shownumber() # 4i + 6j
num3=num1+num2 # aha direct aise add krne se error nhi aayega aha 
               # num3=num1.add(num2) likhna jaruri nahi hai
num3.shownumber() # 5i + 9j


# ab subtract wala karege

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def shownumber(self):
        print(self.real,"i +",self.img,"j")

    def __sub__(self,num2):
        newreal=self.real- num2.real
        newimg=self.img - num2.img
        return Complex(newreal,newimg)

num1=Complex(1,3)
num1.shownumber() # 1i + 3j
num2=Complex(4,6)
num2.shownumber() # 4i + 6j
num3=num1-num2
num3.shownumber() # -31 + -3j