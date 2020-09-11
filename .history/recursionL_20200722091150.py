# recursion has something referred to as the callstack 
'''
so x-->5 
x----->4 
x ---->3
x ---->2 
x ---->1 
x ---> 0 
so when x gets to 0 the function is return which causes call stack to be unwound after the final return statement

'''
def countDown(x):
    if x == 0:
        print("done")
        return 
    else:
        print(x,"....")
        countDown(x-1)
        print("foo",x)

def power(num,pwr):
    if pwr == 0:
        return 1
    else:
        return num *power(num,pwr-1)    
def factorial(num):
    if num == 0:
        return 1 
        
