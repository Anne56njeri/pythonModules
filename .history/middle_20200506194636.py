def get_middle(s):
    word_lenght = len(s)
    
    if word_lenght % 2 == 0:
        first_index_of_middle = word_lenght/ 2 
        second_index_middle = first_index_of_middle + 1
        split_word = s.split(',')

        print(split_word)
        print("Its even")
    else:
        print("Its odd")    
get_middle("test")