import turtle

turtle.penup()
turtle.fd(-100)
turtle.pendown()
turtle.begin_fill()
for k in range(36):
    turtle.fd(200)
    turtle.right(170)
turtle.end_fill()

