

def QuestionsMarks(str):
    numbers = []
    # others = []
    for char in str:
        if char.isdigit():
            numbers.append(int(char))
        elif char == '?':
            numbers.append(char) 
    for i in range(numbers):
        

        
    
             
     
        # break    


    print(numbers.pop()) 
    return str
# keep this function call here 
QuestionsMarks("acc?7??sss?3rr1??????5")