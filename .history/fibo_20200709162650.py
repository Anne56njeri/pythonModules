# solving the fibonaci sequence using recursion and dynamic programming 

# Recursion 
# Base case if n = 1 || n == 2 then fibo is 1 

def fibo(n):
    if n <= 0:
        result = 0
    elif n == 1:
        result = 1 
    else:
        
        result =  fibo(n-1) + fibo(n-2)
        print('result',result)
        print('n',n)
    return result

# print(fibo(5))

# Using dynamic programming 
# we store the fibo of value at n 

def fib(n):
    # we prefill the array where by when then = 0 fib = 0 
    memo = [0,1] 
    # all other items will be 0 
    while

        
               
print(fib(5,[]))               

