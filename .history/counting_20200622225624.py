def counting(str):
    str = str.split('-')
    hour1 = int(convertTo24(str[0]).split(':')[0])
    print('hour1',hour1)
    hour2 = int(convertTo24(str[1]).split(':')[0])

def convertTo24(hour):
    newHour = ''
    if 'am' in hour and hour[:2] == '12':
        newHour = '24'
        newHour += hour[2:5]
    elif ''    
    print(hour)
    print(newHour)
    return newHour    



counting("12:00am-12:00am")    