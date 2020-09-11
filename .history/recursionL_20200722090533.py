# recursion has something referred to as the callstack 
'''
so x-->5 
x----->4 
x ---->3
x ---->2 
x ---->1 
x ---> 0 
so when x gets to 0 the function is return which causes the rest to be called

'''
def countDown(x):
    if x == 0:
        print("done")
        return 
    else:
        print(x,"....")
        countDown(x-1)

countDown(5)          
