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
  # we keep adding until it is invalid cause in this case we want longest substring 
  # a substring is invalid if  len(unique) == uniqueNo +1 
  # at this point we declare unique to be empty then move to the next char which will be 
  # cause there are two pointers left and right ---> so if left = 1 and right = 6
  # then right = left which will be 1   

  uniqueNo = int(str[0])
  left = 1
  right = 1
  str = list(str)
  unique = {}
  while left < len(str) and right < len(str):
    print('left',left,'right',right)
   
   
    if str[right] not in unique:
      unique[str[right]] = 1
    else:
      unique[str[right]] +=1 
    # print(str[left:right]) 
    # print('unique',len(unique),unique) 
    print('string',str[left:right+1])
   
    if len(unique) == uniqueNo:
    #   print(str[left:right+1])
      print ('len',len(unique),'unique',unique)
      
      newArr.append(str[left:right+1])
      
    if len(unique) == uniqueNo + 1:
      

      unique = {}
      
      left +=1 
       
     
    right+=1
  # print(newArr)  
  return  ("".join((max(newArr, key = len))))

KUniqueCharacters("3aabacbebebe")   
     