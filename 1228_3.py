# 반지름을 입력받아서 원을 그리는 코드
import turtle
t = turtle.Turtle()
t.shape("turtle")

w = int(input('사각형의 가로 입력: '))
h = int(input('사각형의 세로 입력: '))
radius = int(input('원의 반지름 입력 : '))
color = input('원의 색깔 입력 : ')

t.color(color)
t.fillcolor(color)
t.begin_fill()
t.fd(w)
t.left(90)
t.fd(h)
t.left(90)
t.fd(w)
t.left(90)
t.fd(h)
t.left(90)
t.end_fill()
'''
t.up()
t.goto(radius, -radius)
t.down()
t.circle(radius)
'''
t.up()
t.goto(0, -radius)
t.down()
t.fillcolor(color)
t.begin_fill()
t.circle(radius)
t.end_fill()

