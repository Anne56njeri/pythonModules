def Hindex(citations):
    result = 0 
    citations.sort()
    for i in range(len(citations)-1,0,-1):
        cnt = len(citations) -i 
        if citations[i] >= cnt:
            result = cnt 
        else:
            break 
    return result        
        
Hindex([3,0,6,1,5])        