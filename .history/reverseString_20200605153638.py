# looping through the array 
# brute method is to switch the positions of the strings using 
# there index's 
# ofcourse should move to h should move to o and vice versa 
# so at any point 0--> length - 1, 1---> length -2 

def reverse(str):
    strLength = len(str)
    end = len(str)-1 
    i = 0 
    while(i < strLength-2 and end >=0 ):
        print(str)
       

        temp = str[i]
       
        str[i] = str[end]
        
        str[end] = temp
       

        
        i +=1
        end -=1
    print(str)    


reverse(["H","a","n","n","a","h"])