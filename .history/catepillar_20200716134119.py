# Counting islands 
# //function functionName()
#  //initialize count to 0
#  //initialize an empty set
#  //loop through the 2D array
#  // if(array[i][j] == 1)
#  // count++
#  // rightneighbour = array[i][j+1]
#  // bottomneighbour = array[i+1][j] 
#  // if(!(set has neighbour)) {
#  // add neighbour to set
#  // functionName(rightneighbour)
#  // functionName(bottomneighbour)
#  // }
def reverse(s):
    answer = ""
    newArr = s.split(" ")
    i = len(newArr)-1
    j = 0
    while i >=0 and j < len(newArr):
        newArr[i]= newArr[i]
        i -=1
    print(answer)    
    print(" ".join(newArr))    


reverse("a good   example")    