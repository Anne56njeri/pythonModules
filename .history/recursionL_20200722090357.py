# recursion has something referred to as the callstack 

def countDown(x):
    if x == 0:
        print("done")
        return 
    else:
        print(x,"....")
        countDown(x-1)

countDown(5)          
