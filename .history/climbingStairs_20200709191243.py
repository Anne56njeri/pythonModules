def climbing(n):
    '''
    Problem:
    Climbing stairs
    You are climbing a stair case.It takes n steps to reach the top 
    Each time you can either climb 1 or 2 steps 
    In how many distinct ways can you climb to the the top 

    1.Define the objective function 
    f(i) --> nu of distinct ways to reach the ith stair 
    2.identify the  base cases
    f(0) = 1
    3. break down to the simplest sub-problem 
    4.Write down a recurrences relation for optimized objective function 
    f(n) = f(n-1) + f(n-2)
    5.Order of excution is 
    ---> Bottom up 
    6.Where to look for the answer 
    dp[n-1]

    '''
    # Make our dp array with the two base cases and we'll prefill 
    dp = [0] * (n+1)
    dp[0] = 1 
    dp[1] = 1 
    # print(dp)
    i = 2 
    while i < len(dp):
        dp[i] = dp[i-1] + dp[i-2]
        i +=1 
    print(dp[n]) 
    '''
    Time complexity is o(n)
    space complexity is o(n) ---. we allocate to an array of size n
    '''   

# climbing(4)    
# Lets optimize our solution by  reducing the space complexity 
# if n was 1000,000 ===> used up 8 mb 


def cli(n):
    # [1,1,2,3]
    #  a b c
    #    a b c 
    # all we need to do is shift the numbers 
    i = 2 
    a = 1 
    b = 1 
    while i <= n:
        c = a +b 
        a = b 
        b = c 
        i+=1 
    print(c) 
    # so for this function the space complexity is o(1)
    # but in this function is n == 1,000,000 then spce = 0.2 mb 
'''
Now we can  either make 1,2,3 steps 
our objective 
f(i) is the number of distinct wys to reach the ith stair 
3. Base cases 
f()
'''


