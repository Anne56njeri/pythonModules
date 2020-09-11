import re 

def three(str):
    strings = str.split(' ')
    for string in strings:
        # replacing any letter with n a
        temp =  re.sub('[A-Z|a-z]', 'a',string)
        # split where there is an a 
        temp = [word for word in temp.split('a') if word !='']
        print('h',temp)
        # means it doesn't have three numbers 
        if len(temp) < 2:
            return 'false'
        temp = ''.join(temp) 
        if len(temp)!=3:
            return 'false'
        print('first',sorted(list(set(temp))),'second',)    
        if sorted(list(set(temp))) != sorted(list(temp)):
            return 'false'
    return 'true'               

        
print(three("2hell6o3 wor6l7d2"))