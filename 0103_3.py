import turtle
t = turtle.Turtle()
t.shape('turtle')

s = input('사각형 또는 원: ')

if s == '사각형':
    width = int(input('가로: '))
    height = int(input('세로: '))
    t.fd(width)
    t.left(90)
    t.fd(height)
    t.left(90)
    t.fd(width)
    t.left(90)
    t.fd(height)
else:
    radius = int(input('반지름: '))
    t.circle(radius)
