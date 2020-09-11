def minCost(days,costs):
    # brute force approach 
    # find if numbers are consecutive 
    # if they are past 7 then means we do a 30 day pass 
    # once they stop being consecutive means to opt for something different 
    # like [1,4,6,7,8,20]
    ways = [0] * days[len(days)-1]
    newDays = set(days)

    for i in range(1,len(ways)):
        newArr = []
        if i -7 > 0:
            total1 = ways[i-7] + costs[2]
        if i-15 > 0:
                


    print(ways) 
minCost([1,4,6,7,8,20],[2,7,15])    