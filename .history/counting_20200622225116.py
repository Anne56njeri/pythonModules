def counting(str):
    str = str.split('-')
    hour1 = int(convertTo24(str[0].split(':')[0]))
def convertTo24(hour):
    newHour = ''
    if 'am' in hour and hour[:2] == '12':
        newHour = '24'
        newHour += hour[]
    print(hour)    



counting("12:00pm-12:00am")    