def nesting(S):
    # first if s is empty return 0 also if count of opening and closing 
    # bracket is not equal return 0 
    # I found what I think is a brilliant solution 
    # count the opening brackets 
    # in the case where you come across a closing bracket and the opening bracket is empty 
    # return 0 
    if S % 2 !=0: return 0 
    opening = 0 
    for i in S:
        if i == "(":
            opening +=1 
        elif opening == 0  and i == ")":
            return 0     
   
                
   
               

print(nesting("(()"))      