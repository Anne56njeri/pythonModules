def iq_test(numbers):
    # check the similarities between the numbers 
    # once you find the similarity 
    #  get the odd one out   
    # there is always a guarntee that there will be on odd number     
    # check for its index in the array   
    # remember the index starts at one not 0 
    even = []
    odd = []
    nums = numbers.split
    uniqueNumber = 0
    for i in numbers:
        nums.append(int(i))


    # for n in numbers:
    #     if n % 2 == 0:
    #         even.append(n)
    #     else:
    #         odd.append(n) 
    # if len(even) > len(odd):
    #     uniqueNumber = odd[0]
    # else:
    #     uniqueNumber = even[0] 
    # indexing =  numbers.index(uniqueNumber) +1  
    # print(indexing)  
    print(nums)  
iq_test("2 4 7 8 10")