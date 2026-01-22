import turtle

# Utgångsläge koordinater (0,0), riktning 0 grader = höger/österut

# Vi definierar en funktion som ritar lite
def rita_lite():

    turtle.pendown() # sätt ner pennan
    turtle.forward(100) # flytta framåt 100 pixlar
    turtle.left(120) # vrid vänster 120 grader
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.penup() # lyft pennan
    # Vad gör följande kod?
    turtle.goto(100, -100) # gå till punkt med koordinater (100, -100)
    turtle.setheading(-45) # sätt riktning till -45 grader (sydost)
    turtle.pendown() # sätt ner pennan
    turtle.begin_fill() 
    # fyll i innanför konturen
    for k in range(4):
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()

rita_lite()
input("Tryck enter för att avsluta") # Väntar in entertangenttryck
# När programmet avslutas stängs grafikfönstret