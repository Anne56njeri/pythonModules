def romanToInt(param):
    totalValue = 0
    romans = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    for i in range(len(param)-1):
        if i+1 == len(param)-1:
            totalValue += romans[param[i+1]]
        if romans[param[i]] < romans[param[i+1]]:
            totalValue -= romans[param[i]]
        elif romans[param[i]] >= romans[param[i+1]]:
            totalValue += romans[param[i]] 
    print(totalValue)          
                
                   

        

romanToInt('')            