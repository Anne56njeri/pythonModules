

def QuestionsMarks(str):
  last_number = None
  nr_of_questions = 0
  
  for l in str:
    if l.isdigit
    
    if l.isdigit():
      print("this is l",l)
      if last_number is not None and (last_number + int(l)) == 10 and nr_of_questions == 3:
        print("this is last number",last_number)
        print("question marks",nr_of_questions)
      else:
        last_number = int(l)
      
      nr_of_questions = 0
    
    if l == '?':
      nr_of_questions += 1
        
  return "false"
   
# keep this function call here 
QuestionsMarks("acc?7??sss?3rr1??????5")