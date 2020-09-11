def balancing(strArr):
    sides = strArr[0][1:-1].split(", ")
    left = int(sides[0])
    right = int(sides[1])
    # here we convert every element in the array to a int as we ignore the first bracket and last bracket 
    # then here we split where  there is a comma and space 

    weights = [int(x) for x in strArr[1][1:-1].split(", ")]
    # we loop through the array 

    for i in range(len(weights)):
        if(left + weights[i] == right) or (right + weights[i] ==left):
            print('weights',weights[i])
    for i in range(len(weights)):
        for j in range(i+1,len(weights)):
            if (left + weights[i] + weights[j] == right ) or (right + weights[i]+weights[j] == left) \
            or (left + weights[i] == right + weights[j]) or (left + weights[j] == right + weights[i]):




balancing(["[5, 9]", "[1, 2, 6, 7]"])    