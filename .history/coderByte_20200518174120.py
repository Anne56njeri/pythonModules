import re 

def QuestionsMarks(str):
  # split where there is a number only 
  numbers = [];
#   splitString = re.split(('\d'),str)
#   print("the split",splitString)
    for char in str:
        if char.isdigit():
            numbers.append(int(char))
            


  # first if statement -Add up the two numbers 
  # Second count the question marks
  # code goes here
  return str
# keep this function call here 
QuestionsMarks("acc?7??sss?3rr1??????5")