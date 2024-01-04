# 한 변의 길이가 100, 70 인 사각형을 그리는 코드
import turtle
t = turtle.Turtle()
t.shape("turtle")

w = int(input('사각형의 가로 입력: '))
h = int(input('사각형의 세로 입력: '))
c = input('사각형의 색깔 입력: ')

t.color(c)
t.fd(w)
t.left(90)
t.fd(h)
t.left(90)
t.fd(w)
t.left(90)
t.fd(h)
t.left(90)
