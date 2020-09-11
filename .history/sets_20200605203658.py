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
    last =len(keys) -1
    lastString = " "
    lastString +=keys[last] + ":" + json.dumps(values[keys[last]])
    

    for i in range(len(keys)-1):
        if keys[i] in values:
            newString += keys[i] + ":"+ json.dumps(values[keys[i]])+","
         
           
    print(newString+lastString)

Strings(["Z:1","B:3","C:3","Z:4","B:2"]) 
