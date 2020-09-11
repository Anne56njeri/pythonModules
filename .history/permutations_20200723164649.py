def perm(A):
    # sort the array 
    if len(A) == 0:
        return 0  
    else:
        maxValue = max(A)
        perm = set(A)
        if len(perm) != maxValue:
            return 0
        else:
            newPerm = list(perm)
            if len(newPerm) == 1 and newPerm[0] == 1:
                return 0
        return 1           

def permu(A):
    counter = [0] * len(A)
    limit = len(A)
    for i in A:
        if not 1 <= i <= limit:
            return 0 
        else:
            if counter[i-1] !=0:
                return 0
            else:
                counter[i-1] = 1
            print(counter)            

           
print(permu([1,1]))

               
    