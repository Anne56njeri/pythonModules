def MinWindowSubstring(strArr):

  # code goes here
  length = len(inp[1])
  check = inp[1]
  contains = 0
  

  while length <= len(inp[0]):
    for i in range(0, len(inp[0]) - length+1):
      sub = inp[0][i:i+length]
      temp = list(sub)
      for i in check:
        if i not in temp:
          contains = 0
          break
        temp.remove(i)
        contains += 1
      if contains:
       return sub

    length += 1

print(MinWindowSubstring(["aaabaaddae", "aed"]))