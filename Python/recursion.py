def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)
# in normal 

def show(n):
    print(n)
show(5) # 5

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(3)


def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(4)) # 24