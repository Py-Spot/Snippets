import requests
import serverdaten
Noten_menge1 = input("Wie viele noten Hast du? ")
Noten_menge2 = int(Noten_menge1)

y = (1)
H = (0)
while y <= Noten_menge2:
    y = y + 1
    anfrage = input("Was ist deine Note")
    H = H + int(anfrage)

server = serverdaten.server_ip
lokal = 'http://127.0.0.1:5000/'
r = requests.post(server, data={'menge': Noten_menge2, 'werte': H})
N = r.text
f = (str(N))


if N > 4.5:
    print("Das sieht garnicht gut aus dein Durschnitt ist " + f)
elif N >= 4.5:
    print ("du solltest an deinen Noten Arbeiten dein Durschnitt ist " + f)
elif N >= 4.0:
    print ("Könnte besser sein dein Durschnitt ist " + f)
elif N >= 3.5:
    print ("nicht gut aber auch nicht schlecht dein Durschschnitt ist " + f)
elif N >= 3.0:
    print ("Dein schnitt liegt ziemlich in der mitte " + f)
elif N >= 2.5:
    print ("Sieht gut aus mach weiter so dein Durschnitt ist " + f)
elif N >= 2.0:
    print ("Sieht sehr gut aus mach weiter so dein Durschnitt ist " + f)
elif N >= 1.5:
    print ("Das sieht supper aus du hast einen durschschnitt von "+ f)
elif N >= 1.0:
    print ("dein schnitt ist wirklich gut dein schnitt ist " + f)


else:
    print ("Da ist wohl was schief gelaufen denn dein schnitt ist " + f)
