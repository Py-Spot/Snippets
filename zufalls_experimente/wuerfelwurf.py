import random
import time
# Die sechstellige liste erstellen um die zalen eins bis sechs darzustellen
zahlen = [0,0,0,0,0,0]

anzahl = 50000000
# die einzelen werte in der liste zufällig um 1 erhöhen
start = time.time()
for n in range(anzahl):
    i = random.randint(1,6)
    if i == 1:
        zahlen[0] += 1
        continue
    if i == 2:
        zahlen[1] += 1
        continue
    if i == 3:
        zahlen[2] += 1
        continue
    if i == 4:
        zahlen[3] += 1
        continue
    if i == 5:
        zahlen[4] += 1
        continue
    if i == 6:
        zahlen[5] += 1
        continue

# za ist der zähler der genutzt wird um denn index in der liste zu deffinieren ( das kobinieren mit enumerate ist das gleiche wie za = za + 1 )
for za, i in enumerate(zahlen):
    # die zahlen die in denn einzelen stellen stehen durch die anzahl teilen für denn prozent wert und auch zu dem prozentwert formatieren
    prozent = i/anzahl
    percentage = "{:.2%}".format(prozent)
    zahlen[za] = percentage

ende = time.time() - start

# Ausgabe
print(f"\n  Es hat {ende} sekunden Gedauert \n")
for zn, i in enumerate(zahlen):
    print(f"  Die Zahl {zn + 1} ist {zahlen[zn]} Vorgekommen")
print("\n")
