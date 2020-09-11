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
    
    keys = sorted(list(values.keys()))
    newString =" "
    for i in keys:
        if i in values:
            newString  = ''.join(map(str))
    print(newString)        
    


Strings(["Z:1","B:3","C:3","Z:4","B:2"]) 
