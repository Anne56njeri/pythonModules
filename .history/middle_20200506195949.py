def get_middle(s):
    word_lenght = len(s)
    split_word = list(s)

    if word_lenght % 2 == 0:
        first_index_of_middle = int(word_lenght/ 2 -1)
        second_index_middle = first_index_of_middle + 1
        two_letters = split_word[first_index_of_middle] + split_word[second_index_middle]
        return two_letters
        
    else:
        first_index_of_middle = int(word_lenght/ 2 )
        a_letter = split_word[first_index_of_middle]
       return a_letter

get_middle("testi")