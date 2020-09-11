def string(str):
    st = list(str)
    count = 0 
    while count < 10:
        for i in range(0,len(st)-1,2):
            pair = st[i] + st[i+1]
            print(pair)
            if pair == 'ab' or pair == 'ba':
                st.pop(i)
                st.pop(i)
                st.insert(i,'c')
                break
            if pair == 'bc' or pair == 'b':
                st.pop(i)
                st.pop(i)
                st.insert(i,'c')
                break
            if pair == 'ab' or pair == 'ba':
                st.pop(i)
                st.pop(i)
                st.insert(i,'c')
                break
        count +=1    


string("abcabc")    