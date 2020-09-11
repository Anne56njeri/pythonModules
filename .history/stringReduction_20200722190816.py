def string(str):
    st = list(str)
    count = 0 
    while count < 20:
        for i in range(0,len(st)-1,2):
            pair = st[i] + st[i+1]
            
            if pair == 'ab' or pair == 'ba':
                del st[i]
                print(i,'i')
                st.insert(i,'c')
                break
            if pair == 'bc' or pair == 'cb':
                st.pop(i)
                st.pop(i)
                print('sec',i,'i')
                st.insert(i,'a')
                break
            if pair == 'ac' or pair == 'ca':
                st.pop(i)
                st.pop(i)
                print('two',i,'i')
                st.insert(i,'b')
                break
            print(st)    
        count +=1 
      


string("abcabc")    