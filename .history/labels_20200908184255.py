def labels(S):
    if len(S) == 0:
        return 0 
    output_arr = []
    last_indices = {}
    for i in range(len(S)):
        if S[i] in last_indices:
            last_indices[S[i]] = i 
        else:
            last_indices[S[]]    

        
    print('last',last_indices)
labels("ababcbacadefegdehijhklij")            