'''
a = 30

if a > 50:
    if a < 100:
        print('50보다 크고 100보다 작음')
    else:
        print('100보다 큼')
else:
    print('50보다 작음')
'''

apple = input('사과의 상태를 입력하세요(신선 or 보통): ')
price = int(input('사과 1개의 가격: '))
pay = 0

if (apple == '신선'):
    if (price < 1000):
        pay = price * 10
        print('총 가격: %d' % pay)
    else:
        pay = price * 5
        print('총 가격: %d' % pay)
else:
    print('사과 안삼')
