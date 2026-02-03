'''
# Funktioner
En funktion är ett stycke "återanvändbar" kod
som givet argumenten a, b som indata returnerar
utdata från funktionen.
f(a,b)
ger ett objekt genom funktionen f med indata a och b

Det finns en uppsjö fördefinierade funktioner i Python,
dels i Pythons standardbibliotek, dels i importerbara moduler.
Utöver det kan man definiera egna funktioner för att
strukturera sitt program.
Definitionen av en funktion börjar med
kodordet 'def'. Funktionens kropp är
sedan indenterad och är slut när indenteringen slutar.
'''

def summan_av(a,b):
    return a+b # kodordet return följs av det värde som funktionen returnerar.

print(summan_av(2,3))

''' När kodordet 'return' stöts på i programflödet
avbryts funktionen och programmet fortsätter
där funktionen anropades, och funktionen
returnerar det värde som uttrycket efter 'return' har.
Finns det ingen returnsats avbryts funktionen vid kodflödets slut 
och det särskilda värdet 'None' returneras.
'''

def skriv_ut_upprepat(a, n):
    for k in range(n):
        print(f'{k}.\t{a}')

b = skriv_ut_upprepat('Hej!', 3)
print('Funktionen returnerar',b)


'''
## Lokala variabler i en funktion
En variabel som definierats i en funktion är lokal,
dvs den går inte att använda utanför funktionen.
Variabler definierade i den del av programmet som anropar funktionen
(globala) är dock tillgängliga inne i funktionen.
Om det finns en lokal variabel med samma namn som en global så har den 
lokala variabeln företräde.
Normalt undviker man användandet av globala variabler
och sänder istället data genom argument till funktionen.
'''

