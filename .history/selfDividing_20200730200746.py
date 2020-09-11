import json 

def dividing(upper,lower):
    newArr = []
    numbers = range(upper,lower+1)
    for i in numbers:
        if i > 0 and i < 10:
            newArr.append(i)
        
        else:
            
            newStr = json.dumps(i)
            print('new',newStr)
            if len(newStr) > 1:
                j = 0
                while j < len(newStr):
                   print('here',newStr[j]) 
                       
                   j+=1 
                   
                          
    print(newArr)
dividing(1,22)        