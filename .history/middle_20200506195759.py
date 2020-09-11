def get_middle(s):
    word_lenght = len(s)
    
    if word_lenght % 2 == 0:
        first_index_of_middle = int(word_lenght/ 2 -1)
        second_index_middle = first_index_of_middle + 1
        split_word = list(s)
        two_letters = split_word[first_index_of_middle] + split_word[second_index_middle]
        print(two_letters)
        print("Its even")
    else:
        first_index_of_middle = int(word_lenght/ 2 -1)
        a_letter = split_word[first_index_of_middle]
        print(a_letter)

get_middle("testi")