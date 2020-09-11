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
    
    while i >=0:
        empty.append(newArr[i])
        
        i -=1
    well = " ".join(empty)
    print("".well.split())    


reverse("a good   example")    