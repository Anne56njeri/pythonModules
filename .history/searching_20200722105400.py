items = [6,20,8,19,56,23,87,41,49,53]

def find_item(item,items):
    for i in range(0,len(items)):
        if item == items[i]:
            return i
    # if the item is not found 
             
    return None        

find_item(87,items)    
find_item(2,items)   