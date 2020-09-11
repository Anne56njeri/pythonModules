import re

def LongestWord(sen):

  # code goes here
  # we are to return the longest word 
  # will first split the sen into words 
  # remove any special charcters 
  sen = re.sub('\W+',' ',sen)
  new_words ={}
  
  # get the length of the word 
  #  to do option we need a for loop 
  #  we should intialize  count/length to zero 

  split_word = sen.split(" ")
  longest_word = "" 
  temp =" "
 
 
  for i in range(len(split_word)-1):
   
    for j in range (i+1,len(split_word)):
    
      if len(split_word[i]) > len(split_word[j]):
        temp = split_word[i]
        split_word[i] = split_word[j]
        split_word[j] = temp 
        
  
    if len(split_word[i]) >= len(split_word[i+1]):
      longest_word = split_word[i]
    else:
      longest_word = split_word[i+1]  
    

    

  # return the word with the longest length 
  return longest_word

# keep this function call here 
LongestWord("beautifule people live here today me ")