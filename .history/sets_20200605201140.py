def Strings(str):
    values = {}
    newArray = []
    keys = []
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
    
    for i in keys:
        if i in values:
            p


Strings(["Z:1","B:3","C:3","Z:4","B:2"]) 
