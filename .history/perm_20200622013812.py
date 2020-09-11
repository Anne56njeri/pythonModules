def sequence(n,k):
    newArr = []

    for i in range(1,n+1):
        newArr.append(i)
    # index == k/n-1!
    answer = " "
    i = 1
    factor = 1
    while i <= n-1:
        factor *=i
        i +=1
    
    index = int(k/factor)
    answer += newArr[index]
    print(answer)
    


sequence(3,3)    