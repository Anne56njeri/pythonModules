def fish(A,B):
    # where A represent the size of fish and B represents the direction of fish 
    i = 0 
    j = 0 
    
    # I'll loop through both arrays 
    # you are intrested in a fish going down 
    # and the fish only eat each other when p > q 
    fish = len(A)
    # break when we reach the end of array A 
    # remove eatten fish 
    while i < len(A) and j <len(B):
        if  B[j] == 1:
