import turtle
t = turtle.Turtle()
t.shape("turtle")
'''
t.home()
t.clear()

t.circle(100, 120)
t.left(60)
t.circle(100, 120)

t.right(60)

t.circle(100, 120)
t.left(60)
t.circle(100, 120)

t.right(60)

t.circle(100, 120)
t.left(60)
t.circle(100, 120)
'''

r = int(input('꽃잎의 반지름: '))
n = 4
t.fillcolor("green")
t.begin_fill()

t.circle(r, 60)
t.left(120)
t.circle(r, 60)
t.left(120)

t.left(90)

t.circle(r, 60)
t.left(120)
t.circle(r, 60)
t.left(120)

t.left(90)

t.circle(r, 60)
t.left(120)
t.circle(r, 60)
t.left(120)

t.left(90)

t.circle(r, 60)
t.left(120)
t.circle(r, 60)
t.left(120)

t.end_fill()
