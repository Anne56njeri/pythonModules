def coinChange(amount):
    coins = [1,5,7,9,11]
    arrayWays = [0] * (amount +1)
    newArray = []
    # Minimum ways to make 0 is 0 
    arrayWays[0] = 0 
    
    for j in  range(len(arrayWays)):
        
        newArray = []
        for i in range(len(coins)):
            if j-coins[i] >=0:
                difference = arrayWays[j-coins[i]] +1
                # print('difference',difference)
                newArray.append(difference)
                
                # print('j',j)
                # print("coins",coins[i])
                # print(newArray)
                # print("================")
        if newArray != []:
            arrayWays[j] = min(newArray)    
            print('min',min(newArray))    
    return arrayWays[amount]    
                

                
               


    # print(arrayWays)

            
    

print(coinChange(25))                    


