# solving the fibonaci sequence using recursion and dynamic programming 

# Recursion 
# Base case if n = 1 || n == 2 then fibo is 1 

def fibo(n):
    if n == 1 or n == 2:
        result = 1 
    else:
        print('result',result)
        result =  fibo(n-1) + fibo(n-2)
    return result

print(fibo(5))

