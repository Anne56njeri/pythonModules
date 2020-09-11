# stacks - where the last item to be added is the first to be reversed 
# reversing an array using 
def stacks(arr):
    arr.append(6)
    arr.append(7)
    newArr = []
    for i in range(len(arr)):
        arr[i].append(arr.pop())
    print(newArr)    


stacks([3,4,5])    