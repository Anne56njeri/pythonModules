import statistics

def mean(arr):
    mean = sum(arr) / len(arr)
    mode = max(arr,key = arr.count)
    print(mean)
    print(mode) 
mean    