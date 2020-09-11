

def QuestionsMarks(str):
    numbers = []
    others = []
    for char in str:
        if char.isdigit() or char == '?':
            numbers.append(int(char) +char)
        if char == '?':
            numbers.append(char) 
        
    
             
     
        # break    


    print(numbers) 
    return str
# keep this function call here 
QuestionsMarks("acc?7??sss?3rr1??????5")