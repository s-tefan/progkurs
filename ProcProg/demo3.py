'''
Sammansatta typer
'''

'''
# Listor
En lista är en ordnad följd av objekt.
Kan skapas direkt med []
En lista kan ändras och utökas. (mutable)
Man kan adressera objekten i en lista, dess element,
genom index. Första elementet har index 0, nästa 1, osv
'''
a = [1,4,67]
print(a, a[0], a[1], a[2])
print(f'Längden av {a} är {len(a)}')
# Man kan lägga till element i slutet av en sträng
a.append(23)
print(a,len(a), a[-1])
# Vi kan gå igenom en lista genom att 
# räkna upp index med range
for n in range(len(a)):
    print(a[n])
# Vi kan också gå igenom listan element för element
for x in a:
    print(x)
# + skapar en ny lista genom att sammanfoga två
c = []
c.extend([6,7,8])
b = a + c
# Man kan också plocka element
print(b)
print(b.pop()) # sista
print(b) 
print(b.pop(0)) # första
print(b)
# Man kan byta ut värden i en lista
b[1]='Haha!'
print(b)




'''
# Tupler
Tupler är som listor en följd av objekt.
Tupler kan inte modifieras (immutable)
'''
a = (1,2,56)
#a[0] = 4 # ger fel
print(a, tuple(), (1,))

'''
# dict: Dictionaries - uppslagsbok
En uppsättning värden som inte är ordnade som en lista
utan istället är indexerade med "nycklar" (keys)
Nycklar och värden kan vara av diverse typer,
kan dock inte vara föränderliga (mutable)
'''
inköp = {"Mjölk": (2, "liter"), "Smör": (3, "kg"), "Bröd": (2, "limpor")}
print(inköp)
print(inköp["Mjölk"])
#print(inköp["Något annat"]) # Ger fel, nyckel saknas
inköp["Glass"] = (2, "liter")
print(inköp)



