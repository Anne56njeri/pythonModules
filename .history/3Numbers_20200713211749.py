import re 

def three(str):
    strings = str.split(' ')
    for string in strings:
        # replacing any letter with n a
        temp =  re.sub('[A-Z|a-z]', 'a',string)
        temp = [word for word in temp.ap]
        print(temp)
three("2hell6o3 wor6l7d2")    