import re 

def three(str):
    strings = str.split(' ')
    for string in strings:
        # replacing 
        temp =  re.sub('[A-Z|a-z]', 'a',string)
        print(temp)
three("2hell6o3 wor6l7d2")    