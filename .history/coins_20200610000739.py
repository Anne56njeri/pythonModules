

def change(amount,coins):
    # create an array of size amount +1
    dp = [0] *(amount + 1)
    print("first dp",dp)
    # at the first index value = 0 
    dp[0] = 1
    print("second dp",dp)
    
    for coin in coins:
        for x in range(coin,amount+1):
            # print("x",x)
            dp[x] += dp[x-coin]
            print("dp in loop --->",dp)
    print(dp[amount])    
    


     
            
            



change(5,[1,2,5])  
