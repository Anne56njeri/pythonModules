def compare(version1,version2):
    # split where there are ,
    # then loop through both of them 
    # if v1 > v2 return 1 
    # if v1 < v2 return -1
    # otherwise return 0 
    v1 = version1.split(".")
    v2 = version2.split(".")

    v1 = [int(i) for i in v1]
    v2= [int(i) for i in v2]
    for a,b in zip(v1,v2):
        if a > b:
            return 1
        elif a < b:
            return -1 
    return 0 
compare("0.1")                



