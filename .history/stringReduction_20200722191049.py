def string(str):
    st = list(str)
    count = 0 
    while count < 20:
        for i in range(0,len(st)-1,2):
            pair = st[i] + st[i+1]
            
            if pair == 'ab' or pair == 'ba':
                
                print('here',i,st[i:i+2])
                del st[i:i+2]
                st.insert(i,'c')
                print('hh',st)
                break
            if pair == 'bc' or pair == 'cb':
                del st[i:i+2]
                st.insert(i,'a')
                break
            if pair == 'ac' or pair == 'ca':
                st.pop(i)
                st.pop(i)
                
                st.insert(i,'b')
                break
            print(st)    
        count +=1 
      


string("abcabc")    