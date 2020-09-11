

def QuestionsMarks(str):
    numbers = []
    for char in str:
        if char.isdigit() || char == '?':
            
            numbers.append(char)
        
     
        # break    


    print(numbers) 
    return str
# keep this function call here 
QuestionsMarks("acc?7??sss?3rr1??????5")