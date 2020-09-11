

def QuestionsMarks(str):
    numbers = []
    others = []
    for char in str:
        if char.isdigit():
            numbers.append(char)
        elif char == '?':
            numbers.append(char) 
    print(numbers)        
    for i in range(len(numbers)):
        if numbers[i] == numbers[i].isdigit():
            print("hello",numbers[i])
            # print(numbers[0:numbers[i]])        

        
    
             
     
        # break    


    print(others) 
    return str
# keep this function call here 
QuestionsMarks("acc?7??sss?3rr1??????5")