

def QuestionsMarks(str):
   a,b = 0,0
   for i in range(len(s)-1):
       for j in range(i,len(s)):
           if s[i].isdigit() and s[j].isdigit() and int(s[i])+int(j[i]) == 10:
               a,b = i,j
new = s[a+1:b+1]
    if new.count('?') == 3:
        return 'true'
    else:
        return 'false'
  
            # print(numbers[0:numbers[i]])        

        
    
             
     
        # break    


    print(new) 
   
# keep this function call here 
QuestionsMarks("acc?7??sss?3rr1??????5")