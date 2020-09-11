def third(arr):
    Min = len(arr[0]) # gets the length of the first word 
    word = arr[0]
    for i in range(len(arr)):
        if len(arr[i]) <= Min:
            word = arr[i] 
    print(word)        



third(["hello","worldd","world","abc"])    