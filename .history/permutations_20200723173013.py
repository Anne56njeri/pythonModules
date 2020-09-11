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
        print('i',i)
        if not 1 <= i <= limit:
            print('herre')
            return 0 
        else:
            # the reason its -1 is cause our range of elements is from 1 to N
            # and index of counter should be from 0 to 
            print('i',i,'i-1',i-1)
            if counter[i-1] !=0:
                print('i',i,'i-1',i-1)    
                print('here')
                return 0
            else:
                counter[i-1] = 1
            print(counter)            

           
print(permu([2,1,3]))

               
    