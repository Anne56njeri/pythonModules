import re 

def QuestionsMarks(str):
  # split where there is a number only 
  
  splitString = re.split('\d',str)
  print("the split",splitString)
  # first if statement -Add up the two numbers 
  # Second count the question marks
  # code goes here
  return str
# keep this function call here 
# print(QuestionsMarks(input()))