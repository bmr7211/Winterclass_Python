'''
# 수수료 구하기 
weight = float(input('짐의 무게: '))
remain = weight - 20
pay = remain * 2000

if (weight > 20):
    print('수수료 %d원' % pay)
else:
    print('수수료 없음')

print('감사합니다.')

# 5% 할인
money = int(input('금액: '))
discount = money * 0.05
price = money - discount

if money >= 100000:
    print('할인금액: %d원, 지불금액: %d원' % (discount, price))
else:
    print('100,000원 이하')

print('안녕히 가세요')
'''
