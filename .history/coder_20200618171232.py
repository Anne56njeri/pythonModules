def MinWindowSubstring(strArr):

  # code goes here
  containing_string = strArr[0]
  search_string = ''.join(sorted(strArr[1]))
  
  min_chars_required = len(search_string)
  
  solution = ''
  solution_array = []
  
  for x in containing_string:
    solution += x
    total_cnt = 0
    # print(solution)
    for c in search_string:
      found_cnt = solution.count(c)
      needed_cnt = search_string.count(c)
      if found_cnt >= needed_cnt:
        total_cnt += 1
    # print(total_cnt)
    if total_cnt == min_chars_required:
      solution_array.append(solution)
      
  # print(solution_array)
  
  solution = ''
  actual_solution_array = []
  for word in solution_array:
    word = word [::-1]
    for x in word:
      solution += x
      total_cnt = 0
      # print(solution)
      for c in search_string:
        found_cnt = solution.count(c)
        needed_cnt = search_string.count(c)
        if found_cnt >= needed_cnt:
          total_cnt += 1
      # print(total_cnt)
      if total_cnt == min_chars_required:
        actual_solution_array.append(solution)
      
      
  answer = min((word for word in actual_solution_array if word), key=len)
  answer = answer [::-1]
  
  return answer
  
MinWindowSubstring(["sz","azjskfzts")