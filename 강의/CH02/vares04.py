import turtle
t=turtle.Turtle()
t.shape("turtle")
distance=int(input("길이를 입력하세요"))

angle3=120
angle4=90
t.fd(distance)
t.left(angle4)
t.fd(distance)
t.left(angle4)
t.fd(distance)
t.left(angle4)
t.fd(distance)
t.left(angle4)

t.up()
t.goto(0,distance)
t.down()


t.fd(distance)
t.left(angle3)
t.fd(distance)
t.left(angle3)
t.fd(distance)
t.left(angle3)


t.up()
t.goto(50,25)
t.down()
t.circle(30)
t.left(90)
