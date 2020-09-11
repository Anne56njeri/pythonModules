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
    for i in range(0,len(A)-1,2):
        #  cater for the last element 
        # if i == len(A)-1:
        #     print('m')
        #     return A[i]
        if A[i] !=A[i+1]:
            return A[i]
print(odd([2,3,2])) 