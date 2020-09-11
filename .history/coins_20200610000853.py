

def change(amount,coins):
    # create an array of size amount +1
    dp = [0] *(amount + 1)
   
    # at the first index value = 0 
    dp[0] = 1
   
    # we loop through the coins array 
    for coin in coins:
        print("coin--->",coin)
        for x in range(coin,amount+1):
            print("x",x)
            dp[x] += dp[x-coin]
            print("dp in loop --->",dp)
    print(dp[amount])    
    


     
            
            



change(5,[1,2,5])  
