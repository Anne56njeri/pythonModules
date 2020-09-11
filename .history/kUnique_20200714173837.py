def unique(str):
    # getting th number of unique char 
    num = int(str[0])
   
    newArr = []
    for i in range(num,len(str) + 1):
        print('i-------->',i)
        for j in range(1,i):
            print('j-->',j)
            if len(set(str[j:i])) == num:
                newArr.append(str[j:i])
    print(max(newArr,key = len))            


# unique("2aabbacbaa") 
# Test cases 
# Input: "3aabacbebebe"
# Output: cbebebe
# Input: "2aabbcbbbadef"
# Output: bbcbbb

def KUniqueCharacters(str):
  # get the number first 
  #  loop through the string 
  # a substring is valid if it has k number of unique char 
  newArr = []
  # how do we validate a substring ?
  # in the case we come accross a valid substring then we add it to our new array 
#   

  uniqueNo = int(str[0])
  left = 1
  right = 1
  str = list(str)
  unique = {}
  while left < len(str) and right < len(str):
   
   
    if str[right] not in unique:
      unique[str[right]] = 1
    else:
      unique[str[right]] +=1 
    # print(str[left:right]) 
    # print('unique',len(unique),unique) 
    # print('string',str[left:right+1])
   
    if len(unique) == uniqueNo:
      print(str[left:right+1])
      print ('len',len(unique),'unique',unique)
      
      newArr.append(str[left:right+1])
      
    if len(unique) == uniqueNo + 1:
      

      unique = {}
      right = left
      left +=1 
       
     
    right+=1
  # print(newArr)  
  return  ("".join((max(newArr, key = len))))

KUniqueCharacters("2aabbacbaa")   
     