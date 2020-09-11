# stacks - where the last item to be added is the first to be reversed 
def stacks(arr):
    arr.append(6)
    arr.append(7)
    newArr = []
    for i in range(len(arr)):
        newArr.append(arr.pop())


stacks([3,4,5])    