def  coinChange(num):
    coins = [1,5,7,9,11]
    # 25 
    arrayWays = [0] * (num +1)
    # there is one way to make coin 0 using 0 
    arrayWays[0] = 1 
    for i in range(len(coins)):
        
    
    print(arrayWays) 


coinChange(16)    
    

      
