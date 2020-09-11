def labels(S):
    if len(S) == 0:
        return 0 
    output_arr = []
    last_indices = {}
    for i in range(len(S)):
        if S[i] in last_indices:
            last_indices[S[i]] = i 
        else:
            last_indices[S[i]] = i 
    start = 0 
    end = 0 
    for i in range(len(S)):
        end = max(end,last_indices[S[i]]) 
        # end = 8 ,when we are at 8,then we get to b its max(8,5) 
        #  end = 8 
        # when we get to that index it means we are at the end of the substring
        # then we now update our start cause we are moving to a new partion
        if i == end:
            output_arr.append(end-start+1)
            start = end+1
        
    print('last',output_arr)
labels("ababcbacadefegdehijhklij")            