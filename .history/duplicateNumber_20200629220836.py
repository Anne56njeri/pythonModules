def duplicate(arr):
    numbers = set()
    i = 0 
    # print(numbers)
    while i < len(arr):

        if arr[i] in numbers:
            return arr[i]  
        else:
            numbers.add(arr[i])   
            
        i +=1    
        # print(numbers)    
          

print(duplicate([1,3,4,2,2]))   