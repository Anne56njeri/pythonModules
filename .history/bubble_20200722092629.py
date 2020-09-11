def bubble(data):
    # TODO: start with the array leneght and decrement each time 
    for i in range(len(data)-1,0,-1):
        for j in range(i):
            if data[j] > data[j+1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
