

def QuestionsMarks(str):
    numbers = []
    for char in str:
        if char.isdigit():
            numbers.append(char)
        if char == '?':
            numbers.append(char)
    splitString = numbers.split(",")   
        # break    


    print(numbers) 
    return str
# keep this function call here 
QuestionsMarks("acc?7??sss?3rr1??????5")