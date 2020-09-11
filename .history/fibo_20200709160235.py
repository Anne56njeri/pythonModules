# solving the fibonaci sequence using recursion and dynamic programming 

# Recursion 
# Base case if n = 1 || n == 2 then fibo is 1 

def fibo(n):
    if n <= 0:
        return 0
    elfif n == 1:
        result = 1 
    else:
        
        result =  fibo(n-1) + fibo(n-2)
        print('result',result)
    return result

print(fibo(5))

