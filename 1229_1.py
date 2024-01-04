'''
a = int(input('첫번째 숫자 입력 : '))
b = int(input('두번째 숫자 입력 : '))
c = int(input('세번째 숫자 입력 : '))

sum_abc = a + b + c
avg = sum_abc / 3

print('합은 %d이고, 평균은 약 %.1f입니다.' % (sum_abc, avg))
print('합 : {0}, 평균 : {1}'.format(sum_abc, avg))


money, coin500, coin100, coin50, coin10 = 0, 0, 0, 0, 0

money = int(input('교환할 돈 : '))

coin500 = money // 500
money %= 500

coin100 = money // 100
money %= 100

coin50 = money // 50
money %= 50

coin10 = money // 10
money %= 10

print('500원짜리 ==> %d개' % coin500)
print('100원짜리 ==> %d개' % coin100)
print('50원짜리 ==> %d개' % coin50)
print('10원짜리 ==> %d개' % coin10)
print('잔돈 ==> %d원' % money)
'''

orange = 50
print('오렌지 50')
box = int(input('박스 개수: '))

orange //= box
remain = orange % box

if remain > 0:
    orange += 1

print('오렌지 %d박스' % orange)
