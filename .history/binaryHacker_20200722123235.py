# time complexity 
# TODO:--> convert to binary 
# count 1 then when you come across 0's assign count to totalCount 
# if count is greater than return  totalCount return count 

def consecutive(num):
    number = f'{num:02b}'
    totalCount = 1
    count = 0
    print(number)
    for i in number:
        if i == '1':
            count +=1 
        elif i == '0':
            count = 0 
        if  totalCount < count:
            print('here')
            totalCount  = count
    print(totalCount)            
consecutive(45)    