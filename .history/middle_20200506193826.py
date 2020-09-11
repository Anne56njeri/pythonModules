def get_middle(s):
    word_lenght = len(s)
    if word_lenght % 2 == 0:
        index_of_middle = word_lenght/2 
        print(index_of_middle)
        print("Its even")
    else:
        print("Its odd")    
get_middle("test")