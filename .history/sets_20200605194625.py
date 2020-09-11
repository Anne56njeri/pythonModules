def Strings(str):
    values = {}
    newArray = []
    keys = []
    for i in str:
     newArray.append(i.split(":"))
    # print(newArray) 
    for j in range(len(newArray)):
        
        if newArray[j][0] in values:
            values[newArray[j][0]] += int(newArray[j][1])
        else:
            values[newArray[j][0]] = int(newArray[j][1])  
    

    print(list(values.keys()))


Strings(["Z:1","B:3","C:3","Z:4","B:2"]) 
