# a tuple is similar to a list but their values cannot be changed 
# keword arguements are arguements that are already defined 

def get_age():
    print("How old are you ?") 
    try:
        age = int(input())
        return age 
    except ValueError:
        return "That was not valid input"      
get_age()        