import json 

def Strings(str):
    values = {}
    newArray = []
    keys = []
    finalArr = []
    for i in str:
     newArray.append(i.split(":"))
     
    for j in range(len(newArray)):
        
        if newArray[j][0] in values:
            values[newArray[j][0]] += int(newArray[j][1])
        else:
            values[newArray[j][0]] = int(newArray[j][1])  
    for k in values:
        keys.append(k)
       
    keys = sorted(keys)
    newString = " "

    for i in len(keys:
        if i in values:
            newString += i + ":"+ json.dumps(values[i]) + ","
         
           
    print(newString)

Strings(["Z:1","B:3","C:3","Z:4","B:2"]) 
