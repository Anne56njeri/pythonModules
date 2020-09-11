def soup(str):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    words = []
    str.lower()
    for l in str:
       words.append(l)
    for i in range(len(words)):
        letterIndex = alphabet.index(words[i])

soup('hello')       
