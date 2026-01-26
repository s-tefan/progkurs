import random

# Denna funktion kommer inte att fungera eftersom listan modifieras under hand
def rensa_fel(aplista):
    for i,k in enumerate(aplista):
        if k < 10:
            aplista.pop(i)

def rensa(aplista, update = True):
    nylista = []
    for i,k in enumerate(aplista):
        if not(k < 10):
            nylista.append(k)
    if update:
        aplista = nylista
    else:
        return nylista

minlista = [random.randint(0,20) for n in range(20)]
print(minlista)
rensa(minlista)
print(minlista)

