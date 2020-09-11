

def QuestionsMarks(str):
    numbers = []
    for char in str:
        if char.isdigit():
            
            numbers.append({"number":int(char)})
        if char == '?':
            numbers.append({"mark":char}) 
        for num in numbers:
          print(num.number)
          print  
    
             
     
        # break    


    print(numbers) 
    return str
# keep this function call here 
QuestionsMarks("acc?7??sss?3rr1??????5")