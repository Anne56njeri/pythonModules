def counting(str):
    str = str.split('-')
    hour1 = convertTo24(str[0])

def convertTo24(hour):
    newHour = ''
    if 'am' in hour and hour[:2] == '12':
        newHour = '24'
        newHour += hour[2:5]
    print(hour)
    print(newHour)
    return newHour    



counting("12:00pm-12:00am")    