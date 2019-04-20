import turtle
t=turtle.Turtle()
t.shape("turtle")

x_1 = int(input("x1: "))
y_1 = int(input("y1: "))
x_2 = int(input("x2: "))
y_2 = int(input("y2: "))

also = ((x_1 - x_2)**2 + (y_1 - y_2)**2)**0.5
t.up
t.goto(x_1,y_1)
t.down

t.goto(x_2,y_2)

t.write('선의 길이는'+str(also))
