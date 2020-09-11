def brackets(str):
    # "{[()()]}"
    if len(str) == 0:
        return 1 
    countSopen = 0 
    countSclosed = 0 
        
