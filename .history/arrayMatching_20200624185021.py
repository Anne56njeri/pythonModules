def ArrayMatching(strArr):
    liste1=[int(n) for n in str(strArr[0]).replace('[','').replace(']','').split(',')]
    liste2=[int(n) for n in str(strArr[1]).replace('[','').replace(']','').split(',')]
    if len(liste1) >=len(liste2):
        listeMax=liste1
        listeTwo=liste2
    else:
        listeMax=liste2
        listeTwo=liste1

    for i in range(0, len(listeTwo)):
        listeMax[i]+=listeTwo[i] 

    return '-'.join(str(x) for x in listeMax)