'''
Given a linked list,swap every two adjacent nodes and returns its head 
you may not modify the values in the list nodes  only nodes itself may be changed
'''
import string
def swap(string):
    lower_list = string.ascii_lowercase
    output = ""
    for c in string.lower():
        if c in lower_list:
            output += str(lower_list.find(c)+1)
        else:
            output +=c 

    print(output)
swap("hello 45")