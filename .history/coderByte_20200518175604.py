import re 

def QuestionsMarks(str):
    splitString = re.split(('\d'),str) 
    numbers = [];
    for char in str:
        if char.isdigit():
            numbers.append(char)
            if char == '?'
        break    


    print(numbers) 
    return str
# keep this function call here 
QuestionsMarks("acc?7??sss?3rr1??????5")