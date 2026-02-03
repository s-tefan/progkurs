'''
== Utskrift på skärm ==
'''
print("Hello, world!")
print(1, '+', 2, '=', 1+2)

''' Extra: Med s.k. f-strängar kan man stoppa in värden i en mall. '''
print(f'{1} + {2} = {1+2}')

# Kopplar tal-värden till variabelnamn
a = 1
b = 2
print(f'{a} + {b} = {a+b}')


'''
== Inmatning av text ==
För att få input från användaren kan man använda input()
som returnerar den text som skrivs in i ett objekt av typ 'str'.
Funktionen print() skriver ut värden.
Ger man flera värden med komma emellan skrivs värdena ut med mellanslag emellan.
'''

namn = input('Vad heter du? ')
print('Hej,', namn, '!')
'''
För att ta in ett numeriskt värde att räkna med behöver strängen tolkas som ett tal,
och omvandlas till ett objekt som är en taltyp, 'int' (heltal) eller 'float' (bråk)
vilket görs med funktionerna int() respektive float().
'''

ålder = int(input('Hur många år gammal är du?'))
print(f'{namn} är {ålder} år gammal. För tre år sedan var {namn} {ålder-3} år gammal.')

if ålder >= 90:
    print(f'{namn} är gammal.')
    print('Så gammal!')
elif ålder >= 30:
    print(f'{namn} är medelålders.')
    print('Inte lika gammal, men...')
else:
    print(f'{namn} är ung.')

print('Färdig')

