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
    
    newArr = s.split(" ")
    empty = []
    i = len(newArr)-1
    j = 0
    while i >=0 and j < len(newArr):
        empty.append(newArr[i]
        j +=1
        i -=1
   
    print(" ".join(empty))    


reverse("a good   example")    