'''
score = int(input('점수 입력: '))

if score >= 90:
    print('A', end=" ")
elif score >= 80:
    print('B', end=" ")
elif score >= 70:
    print('C', end=" ")
elif score >= 60:
    print('D', end=" ")
else:
    print('F', end=" ")

print('학점입니다.')


day31 = [1, 3, 5, 7, 8, 10, 12]
day30 = [4, 6, 9, 11]
day29 = [2]

month = int(input('월 입력: '))

if month in day31:
    print('월의 날 수는 31일')
elif month in day30:
    print('월의 날 수는 30일')
else:
    print('월의 날 수는 29일')
'''

month = int(input('월 입력: '))

if (month == 2):
    print('월의 날 수는 29일')
elif (month == 4 or month == 6 or month == 9 or month == 11):
    print('월의 날 수는 30일')
else:
    print('월의 날 수는 31일')
    
