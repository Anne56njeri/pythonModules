

def change(amount,coins):
    dp = [0] *(amount + 1)
    print("first dp")
    dp[0] = 1
    for coin in coins:
        for x in range(coin,amount+1):
            dp[x] += dp[x-coin]
    print(dp[amount])    
    


     
            
            



change(5,[1,2,5])  
