def countDown(x):
    if x == 0:
        print("done")
        return 
    else:
        print(x,"....")
        countDown(x-1)  
