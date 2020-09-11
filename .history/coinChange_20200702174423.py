def  coinChange(num):
    # coins = [1,5,7,9,11]
    coins = 
    # 25 
    arrayWays = [0] * (num +1)
    # there is one way to make coin 0 using 0 
    arrayWays[0] = 1 
    for i in range(len(coins)):
        for j in range(len(arrayWays)):
            if coins[i] >= j:
                sum = arrayWays[j- coins[i]] + arrayWays[j]
                arrayWays[j] +=sum 

    
    print(arrayWays) 


coinChange(16)    
    

      
