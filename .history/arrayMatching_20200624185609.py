
def ArrayMatching(strArr):
    liste1=[int(n) for n in str(strArr[0]).replace('[','').replace(']','').split(',')]
    liste2=[int(n) for n in str(strArr[1]).replace('[','').replace(']','').split(',')]
    if len(liste1) >=len(liste2):
        listeMax=liste1
        listeTwo=liste2
    else:
        listeMax=liste2
        listeTwo=liste1
    # looping through the smaller array 
    print('bigger Array',listeMax)
    for i in range(0, len(listeTwo)):
        # we are replacing the values of the larger array  with the sum of the two arrays
        # up to the length of the small array 

        listeMax[i]+=listeTwo[i] 
        print('max',listeMax)
    # list comprehension we add the dash them up
    return '-'.join(str(x) for x in listeMax) 

print(ArrayMatching(["[1, 2, 5, 6,7,8]", "[5, 2, 8, 11]"]))    