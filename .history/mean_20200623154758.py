import statistics

def mean(arr):
    mean = sum(arr) / len(arr)
    mode = max(arr,key=a)
    print(mean)
    print(mode) 
mean([4,4,4,6,2])    