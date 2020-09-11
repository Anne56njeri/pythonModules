def canWinNim(n):
    # you get the first turn 
    # you can remove 1,2,3 stones 
    # the one to remove the last stone wins 
    if n % 4 == 0:
        return False