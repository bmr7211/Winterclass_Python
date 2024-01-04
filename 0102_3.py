'''
gender = input('성별 입력: ')

if (gender == '여자'):
    print(gender)
else:
    print(gender)
'''

import turtle
t = turtle.Turtle()
t.shape("turtle")
t.left(90)

control = input('방향 입력: ')

if (control == 'left'):
    t.left(90)
    t.fd(100)
else:
    t.right(90)
    t.fd(100)
