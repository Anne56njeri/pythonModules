def Strings(str):
    values = {}
    newArray = []
    for i in str:
     newArray.append(i.split(":"))
    # print(newArray) 
    for j in newArray:
        if newArray[j][0] in values:
            values[j][0] = newArray[j]




Strings(["A:1","B:3","C:3","A:4","B:2"]) 
