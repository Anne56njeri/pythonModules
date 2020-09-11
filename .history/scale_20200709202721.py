def balancing(strArr):
    sides = strArr[0][1:-1].split(", ")
    left = int(sides[0])
    right = int(sides[1])
    # here we convert every element in the array to a int as we ignore the first bracket and last bracket 
    # then here we split where 
    weights = [int(x) for x in strArr[1][1:-1].split(", ")]
    print(weights)
balancing(["[5, 9]", "[1, 2, 6, 7]"])    