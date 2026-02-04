import turtle

turtle.speed(30)
turtle.width(7)
turtle.color("purple")
turtle.forward(200)
turtle.left(90)

turtle.forward(200)
turtle.left(90)

turtle.forward(200)
turtle.left(90)

turtle.forward(200)
turtle.left(90)

turtle.forward(70)
turtle.color("yellow")
turtle.begin_fill()
turtle.left(90)
turtle.forward(120)
turtle.right(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(120)
turtle.end_fill()

turtle.penup()
turtle.goto(200, 200)
turtle.pendown()
turtle.color("blue")
turtle.begin_fill()
turtle.right(150)
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.end_fill()

turtle.penup()
turtle.goto(60, 50)
turtle.pendown()

turtle.width(3)
turtle.color("red")
turtle.begin_fill()
turtle.right(60)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()

turtle.penup()
turtle.goto(140, 50)
turtle.pendown()
turtle.begin_fill()
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()




turtle.exitonclick()