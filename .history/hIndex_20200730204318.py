def Hindex(citations):
    result = 0 
    citations.sort()
    for i in range(len(citations),0,-1):
        cnt = len(citations) -i 
        print('i',i,'cnt')
        
Hindex([3,0,6,1,5])        