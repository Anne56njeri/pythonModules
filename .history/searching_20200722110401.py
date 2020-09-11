items = [6,20,8,19,56,23,87,41,49,53]

# for an unordered list 

def find_item(item,items):
    for i in range(0,len(items)):
        if item == items[i]:
            return i
    # if the item is not found 
             
    return None        

print(find_item(87,items))    
print(find_item(250,items))   
#  for a sorted list 
def find(item,items):
    # get the list size 
    listSize = len(items)-1
    lower = 0 
    upper = listSize 
    # this loop will execute when the two pointers do not meet 
    while lower <= upper:
        # TODO: calculate the middle point 
        midPoint = (lower + upper) // 2
        if items[midPoint] == item:
            return midPoint
        if item > items[midPoint]:
            lower = midPoint+1
        else:
            upper = midPoint -1    
    if lower > upper:
        return None    

print(find(23,items))      
print(find(,items))        


