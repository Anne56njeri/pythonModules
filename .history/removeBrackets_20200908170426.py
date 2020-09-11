def remove(str):
       stackB.append(i)
            
    while stackA !=[] and stackB !=[]:
        if stackB[-1] !=stackA[-1]:
            stackA.pop()
            stackB.pop()
        
    if stackA != []:
        return len(stackA)
    elif stackB != []:
        return len(stackB)  
    elif stackA == [] and stackB == []:
        return 0      

    


print(remove(")(()"))               