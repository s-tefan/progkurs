'''
Data i python är objekt.
Ett objekt har ett unikt id och en typ.
Ett objekt kan refereras till genom ett variabelnamn.
De vanligaste enkla typerna är
    'str': En sträng av tecken. Ex: 'En teckensträng'
    'int': Ett heltal. Ex: 13 skapar ett heltal
    'float': Ett 'flyttal' som representerar ett bråktal. Ex: 3.45 skapar ett flyttal.
    'bool': Är antingen True eller False
'''
print(type('En teckensträng'), type(13), type(3.45))

'''
Till ett objekt kan man koppla ett variabelnamn.
Så länge ett objekt är kopplat till ett variabelnamn finns det i minnet, annars kan det städas bort.
'''
a = 23
b = a # Nu refererar a och b till samma objekt, heltalet 23
print(a,b,id(a),id(b),type(a),type(b))

b = 42 # Nu refererar b till ett annat objekt, heltalet 42
print(a,b,id(a),id(b),type(a),type(b))

a = "Hejsan" # Nu refererar a till ett annat objekt, en teckensträng
print(a,b,id(a),id(b),type(a),type(b))

2 = 2.0
      

'''
Lägga ihop teckensträngar
'''
s = "svejsan"
t = a+' '+s
print(t)
tt = f'{a} {s}'
print(tt)

'''
Aritmetiska operationer på tal
'''
a = 23
b = a + 1
print(a,b)
b = b + 1  # eller b += 1
print(a, b)
print((23+41)*2, 23+41*2)
print(2*3, 2/3, 2**3, 2**(-3), 2**0.5)

'''
bool: Logiska värden (booleska eller boolean, efter George Boole)
Sanningsvärdet av ett påstående (en utsaga)
'''
print(1==1, 1==2, 1!=2, 1>2, 1>=2, 1<2, 1<=2)

'''
Booleska värden används till exempel vid selektion:
'''
a = int(input("Ge mig ett tal! ")) 
# obs typkonversion till int!
if a == 0:
    print(f"{a} är lika med noll.")
elif a > 0:
    print(f"{a} är ett positivt tal.")
elif a < 0:
    print(f"{a} är ett negativt tal.")
else:
    print("Jag förstår mig inte på talet {a}.")

'''
Strängar och tal kan tolkas som boolska värden:
En tom sträng "" tolkas som False, annars som True.
Heltalet 0 och flyttalet 0.0 tolkas som False, andra tal som True.
'''
print(bool(0), bool(0.1))

'''
while-loop
Att upprepa ett programblock så länge en boolesk variabel är sann
'''

n = 0
while n <= 3:
    print(n)
    n = n+1
print("Nu är det slut!")

'''
loop ett visst antal gånger
'''
for n in range(6): # Startar på noll upp till innan 6
    print(f'{n} i kvadrat är {n**2}')

for n in range(-2,3): # Startar på -2 upp till innan 3
    print(f'{n} i kvadrat är {n**2}')

for n in [5,2,8,2,5]: # loopa igenom en lista
    print(f'{n} i kvadrat är {n**2}')

