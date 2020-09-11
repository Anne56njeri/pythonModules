def twoCity(nums):
    minimum = 0
    for i in nums:
        minimum += min(i)
        print(min(i))
    print(minimum)






twoCity([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]])    