

def QuestionsMarks(str):
    numbers = []
    for char in str:
        if char.isdigit():

            numbers.append(int(char))
        if char == '?':
            count = 0
            count =+1

            numbers.append(count) 
    
             
     
        # break    


    print(numbers) 
    return str
# keep this function call here 
QuestionsMarks("acc?7??sss?3rr1??????5")