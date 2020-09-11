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

def fib(n,memo):
    if memo[n] != None:
        return memo[n]
    if n == 1 or n == 2:
        return 1 
            

    if n <= 0:
       memo[n] = 0 
    elif n == 1:
        memo[n] = 1 
    else:
        
        memo[n] = fib(n-1,memo) + fib(n-2,memo)
    print('memo',memo)
    return memo[n]    
               
print(fib(5,[]))               

