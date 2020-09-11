def Hindex(citations):
    result = 0 
    citations.sort()
    print(citations)
    for i in range(len(citations)-1,0,-1):
        cnt = len(citations) -i 
        print('i',i,'cnt',cnt)

        if citations[i] >= cnt:
            result = cnt 
        else:
            break 
    print(result        
        
Hindex([3,0,6,1,5])        