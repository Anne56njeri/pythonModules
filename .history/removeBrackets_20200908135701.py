def remove(str):
    # find how many make a complete pair 
    # subtract that from the total 
    total = len(str)
    opening ="("
    closing = ")"
    for i in range(len(str))