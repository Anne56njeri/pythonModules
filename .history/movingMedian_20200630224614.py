def MovingMedian(l):
  k = l.pop(0)
  answer = []
  for i in range(len(l)):
    if i < k:
      a = l[:i]
      a.append(l[i])
      a = sorted(a)
    else:
      a = l[i-(k-1):i]
      a.append(l[i])
      a = sorted(a)
    #print(a)
    b = len(a)
    if len(a) % 2 != 0:
      median = str(int(a[int((b-1)/2)]))
    else:
      median = str(int((a[int(b/2)] + a[int((b/2) -1)])/2))
    answer.append(median)
    
  return ','.join(answer) 
print(MovingMedian([3,1,3,5,10,6,4,3,1])) 