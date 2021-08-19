import turtle

pen = turtle.Pen()
pen.speed(100)

width = 10  # 格子宽度
count = 37  # 横向纵向格子数

o = width * count / 2  # 开始绘制原点

for i in range(count + 1):
    pen.penup()
    pen.goto(-o, o - i * width)
    pen.pendown()
    pen.goto(o, o - i * width)

for i in range(count + 1):
    pen.penup()
    pen.goto(-o + i * width, o)
    pen.pendown()
    pen.goto(-o + i * width, -o)

pen.hideturtle()
turtle.done()