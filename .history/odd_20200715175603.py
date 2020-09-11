# def odd(A):
#     # return the value that doesn't have a pair 
#     # a dictionary to keep track of the number of times 
#     # an element has been repeated 
#     newDict = {}
#     if len(A) <= 0:
#         return 0
#     for i in A:
#         if i in newDict:
#             newDict[i] +=1
#         else:
#             newDict[i] = 1
#     for i in newDict:
#         if newDict[i] == 1:
#             return i 
        
#     return 0    
                     



 
def odd(A):
    if len(A) == 1:
        return A[0]
    # we sort the array     
    A = sorted(A)
    print(A)
    # we loop as we skip two items  
    for i in range(0,len(A),2):
        if i + 1 = =len(A):
            return A[i]
        print(i) 
print(odd([9,3,9,3,9,7,9])) 