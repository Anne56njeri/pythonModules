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
    
