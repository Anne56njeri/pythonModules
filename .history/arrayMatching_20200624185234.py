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

    for i in range(0, len(listeTwo)):
        listeMax[i]+=listeTwo[i] 
        print('max'listeMax)

    return '-'.join(str(x) for x in listeMax) 

print(ArrayMatching(["[1, 2, 5, 6,7,8]", "[5, 2, 8, 11]"]))    