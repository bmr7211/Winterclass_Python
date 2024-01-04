# 정삼각형 그리기 
import turtle
t = turtle.Turtle()
t.shape("turtle")

t.color("red")
t.fd(150)
t.left(120)
t.fd(150)
t.left(120)
t.fd(150)

# 초기화1
t.home()
t.clear()

# 정사각형 그리기
t.color("blue")
t.fd(100)
t.left(90)
t.fd(100)
t.left(90)
t.fd(100)
t.left(90)
t.fd(100)

# 초기화2
t.up()
t.goto(-200,-200)
t.down()

# 원 그리기
t.color("green")
t.circle(100)

# 원 두개 그리기
t.up()
t.goto(0,-200)
t.down()
t.color("purple")
t.circle(100)
