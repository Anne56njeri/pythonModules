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
    while len(memo) < n+1:
        memo.append(0)
    print(memo) 
    i = 2
    while i < len(memo):
        memo[i] = memo[i-2] + memo[i-1]
    # at this point we have our array now all we have to do is fill it in 
       

        
               
print(fib(5))               

