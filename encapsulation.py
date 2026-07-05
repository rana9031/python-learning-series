# create account class with 2 attributes balance and account no , create 
# method for debit,credit and printing the balace.

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
    #debit method
    def debit(self,amount):
        self.balance-=amount
        print("Rs",amount,"was debited")
    
    #credit method
    def credit(self,amount):
        self.balance+=amount
        print("Rs",amount,"was credit")
    
    def get_bal(self):
        return self.balance
    
acc1=Account(10000,12345)
print(acc1.balance)
print(acc1.account_no) # output = 10000
                       #          12345

# same question dusri tarah se solve

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
    
    def debit(self,amount):
        self.balance-=amount
        print("Rs",amount,"was debited")
        print("total balace=",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("Rs",amount,"was debited")
        print("total balace=",self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1=Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)  

'''
10000
12345
Rs 1000 was debited
total balace= 9000
Rs 500 was debited
total balace= 9500
Rs 40000 was debited
total balace= 49500
'''