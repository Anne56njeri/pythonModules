def perm(arr):
    # sort the array 
    arr.sort()
    perm = set(arr)
    for i in range(len(perm)):
        print(perm[i])
perm([4,1,3,2])