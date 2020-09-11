def search(root,value):
    numbers = sorted(root)
    found = []
    # lower bound
    l = 0 
    u = len(root) -1

    while l <= u:
        mid = (l+u) // 2
        if numbers[mid] == value:
            append(numbers[mid])
            return numbers[mid]
        else:
            if value > numbers[mid]:
                l = mid + 1
            else:
                u = mid - 1

    return "Null"                     

    print(numbers)


search([4,2,1,7,3],2)    