import turtle
t=turtle.Turtle()
t.shape("turtle")
n = int(input('몇각형을 만드시고 싶으세요?(3이상)'))
for i in range(n):
    if n >10:
        t. forward(50)
    else:
        t.forward(100)
    t.left(360/n)

