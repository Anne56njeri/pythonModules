# stacks - where the last item to be added is the first to be reversed 
# reversing an array using stacks
# def stacks(arr):
#     arr.append(6)
#     arr.append(7)
#     newArr = []
#     for i in range(len(arr)):
#         newArr.append(arr.pop())
#     print(newArr)    


# stacks([3,4,5])  
# ========================================================
# Queue 
from collections import deque

def Queue():
    queue = deque(["Eric","John","Michael"])
    queue.append("Terry") # Terry arrives 
    queue.append("Graham") # Graham arrives 
    queue.po
