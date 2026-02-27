# 1 write a recursion functuon to calculate the sum of first n natural number
def cal_sum(n):
    if(n==0):
        return
    print(n)
    cal_sum(n-1)
cal_sum(5)

def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1)+n
sum=calc_sum(5)
print(sum) # 15

# 2 write a recursive function to print all the elements in a list
# hint- use list and index as parameter

def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
fruits=["mango","litchi","apple","banana"]
print_list(fruits)