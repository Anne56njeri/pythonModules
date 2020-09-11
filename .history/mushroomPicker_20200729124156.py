'''
You are given a non-empty, zero-indexed array A of n (1 � n � 100 000) integers
a0, a1, . . . , an−1 (0 � ai � 1 000). This array represents number of mushrooms growing on the
consecutive spots along a road. You are also given integers k and m (0 � k, m < n).
A mushroom picker is at spot number k on the road and should perform m moves. In
one move she moves to an adjacent spot. She collects all the mushrooms growing on spots
she visits. The goal is to calculate the maximum number of mushrooms that the mushroom
picker can collect in m moves.
For example, consider array A such that:
''' 
def mushroom(A,k,m):
    # A - is the array 
    # k- is there position 
    # m - number of moves they can make 
    n = len(A)
    result = 0 
    pref = [0] * n 
    pref[0] = A[0]
    for i in range(1,n):
        pref[i] = A[k-1]

    for k in range(1,n):
        A[k] = A[k-1] + A[k]
    print(A) 
mushroom([2,3,7,5,1,3,9],4,6)    