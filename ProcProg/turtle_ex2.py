def follow_path(pl):
    for c in pl:
        comm = c[0], num = c[1] # eller: comm, num = c
        if comm == 'f':
            turtle.forward(num)
        elif comm == 'b':
            turtle.backward(num)
        elif comm == 'l':
            turtle.left(num)
        elif comm == 'r':
            turtle.right(num)
        else:
            pass

#Nu kör vi funktionen
rita_lite()    
#Vi stannar till så inte programmet avslutas innan vi säger till.
input('Tryck return för att avsluta.')


follow_path([('l',30),('f',50),('l', 60)])