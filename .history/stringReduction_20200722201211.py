def string(str):
    st = list(str)
    count = 0 
    while count < 20:
        for i in range(0,len(st)-1):
            pair = st[i] + st[i+1]
            print('pair',pair)
            
            if pair == 'ab' or pair == 'ba':
                
                print('here',i,st[i:i+2])
                del st[i:i+2]
                st.insert(i,'c')
                print('hh',st)
                break
            if pair == 'bc' or pair == 'cb':
                del st[i:i+2]
                print('here',i,st[i:i+2])
                st.insert(i,'a')
                print('hh',st)
                break
            if pair == 'ac' or pair == 'ca':
                del st[i:i+2]
                
                st.insert(i,'b')
                break
            print(st)    
        count +=1 
      


string("abcabc")    