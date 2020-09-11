def MinWindowSubstring(inp):

  # code goes here
  length = len(inp[1]) #4
  
  check = inp[1]
  contains = 0
  

  while length <= len(inp[0]):
    for i in range(0, len(inp[0]) - length+1):
      sub = inp[0][i:i+length]
      print(sub)
      temp = list(sub)
      for i in check:
        if i not in temp:
          contains = 0
          break
        temp.remove(i)
        print("temp",temp)
        # contains += 1
        print(contains)
      if contains:
       print("sub",sub)
       return sub

    length += 1

print(MinWindowSubstring(["aaabaaddafe", "aedd"]))