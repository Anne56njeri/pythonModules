row = [-1,-1,-1,0,1,0,1,1]
col = [-1,1,0,-1,-1,1,0,1]


def BoggleSolver(strArr):
  lookup =  strArr[0]
  lookup = lookup.split(", ")
  
  allWords = set()
  board = []
  # we construct a matrix to determin whethere visited or not
  processed = [[False for x in range(4)]for y in range(4)]
  # print("pro",processed)
  for m in lookup:
    ans = []
    for n in m:
      ans.append(n)
    board.append(ans)  
  
  # this stores all the possible movements x and y
  for i in range(4):
    for j in range(4):
      wordGen(board,allWords,processed,i,j)
  print('all',allWords)

def wordGen(lookup,allWords,processed,i,j,path=" "):
  processed[i][j] = True 
  path = path + lookup[i][j]
  allWords.add(path)
  for k in range(8):
    if safe(i + row[k], j + col[k],processed):
      wordGen(lookup,allWords,processed,i + row[k],j + col[k],path)
  processed[i][j] = False
# this function makes sure we are not out of bound and the cell we want to go to has not been processed  
def safe(i,j,processed) :
  # return a boolean
  return (0 <= i < 4) and(0 <= j < 4) and not processed[i][j] 
# to generate possible words we use a recursive functions that moves in diff directions 
     
Bo