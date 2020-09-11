def search(root,value):
    numbers = sorted(root)
    found = []
    # lower bound
    l = 0 
    u = len(root) -1

    while l <= u:
        mid = (l+u) // 2
        if numbers[mid] == value:
            return numbers[mid]
        else:
            if value > numbers[mid]:
                    

    print(numbers)


search([4,2,1,7,3],2)    