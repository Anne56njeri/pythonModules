def balancing(strArr):
    sides = strArr[0][1:-1].split(", ")
    left = int(sides[0])
    right = int(sides[1])
    weights = [int(x) for x in strArr[1][]]
balancing(["[5, 9]", "[1, 2, 6, 7]"])    