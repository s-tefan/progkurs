import turtle
x=50
y=100
angle=90
steps=10
turtle.penup() # pennan lyfts från papperet
turtle.pendown() # pennan sätts ner på papperet
turtle.goto(x,y) # sköldpaddan flyttas till koordinater (x,y)
turtle.right(angle) # sköldpaddan vrids åt höger <angle> grader
turtle.fd(steps) # Sköldpaddan flyttas <steps> steg (pixlar) framåt
input("press Enter to continue")
# Grafikfönstret stängs när programmet avslutas.