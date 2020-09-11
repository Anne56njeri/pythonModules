def passingCars(A):
    zeroes = 0 
    pairs_passed = 0
    for i in A:
        if i == 0:
            zeroes +=1 
            print("zeroes",zeroes)
        elif i == 1:
            pairs_passed +=zeroes
            print("zeroes",zeroes) 
    print(pairs_passed)        


passingCars([0,1,0,1,1])    