

def QuestionsMarks(str):
  last_number = None
  nr_of_questions = 0
  
  for l in str:
    
    if l.isdigit():
      if last_number is not None and (last_number + int(l)) == 10 and nr_of_questions == 3:

        print (last_number,l)
      else:
        last_number = int(l)
      
      nr_of_questions = 0
    
    if l == '?':
      nr_of_questions += 1
        
  return "false"
   
# keep this function call here 
QuestionsMarks("acc?7??sss?3rr1??????5")