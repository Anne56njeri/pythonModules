# recursion has something referred to as the callstack 
'''
so x-->5 
x----->4 
x ---
'''
def countDown(x):
    if x == 0:
        print("done")
        return 
    else:
        print(x,"....")
        countDown(x-1)

countDown(5)          
