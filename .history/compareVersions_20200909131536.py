def compare(version1,version2):
    # split where there are ,
    # then loop through both of them 
    # if v1 > v2 return 1 
    # if v1 < v2 return -1
    # otherwise return 0 
    v1 = version1.split(".")
    v2 = version2.split(".")
    v1 = [int(i)]


