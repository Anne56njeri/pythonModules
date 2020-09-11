import re 

def three(str):
    strings = str.split(' ')
    for string in strings:
        # replacing any letter with n a
        temp =  re.sub('[A-Z|a-z]', '',string)
        # split where there is an a 
        temp = [word for word in temp.split('a') if word !='']
        # means it doesn't have three numbers 
        if len(temp) < 2:
            return 'false'

        print(temp)
three("2hell6o3 wor6l7d2")    