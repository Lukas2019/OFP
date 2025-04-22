import random
## Was brauchen wir für das "Goofspiel"?

# Kartenspiele für die zwei Spieler verteilen, 
spieler1_kartenspiel = [1,2,3,4,5,6,7,8,9,10,11,12,13]
spieler2_kartenspiel = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# Kartenspiel für die Preiskarten
# Kartenspie = Liste von Zahlen 1,2,3,4,...,13
preiskarten = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# Die Preiskarten werden gemischt
random.shuffle(preiskarten)

## Verrückte Computerstrategie für beide Spieler:
# Ziehe nur zufällige KArten
random.shuffle(spieler1_kartenspiel)
random.shuffle(spieler2_kartenspiel)

# Möglichkeit Punkte der Spieler zu speichern 
spieler1_punkte = 0
spieler2_punkte = 0

####  Dies ist eine Runde -  die wird immer wiederholt bis alle 
# Karten aufgebraucht sind
while preiskarten:
    # Ziehe die oberste Preiskarte -> Variable preiskarte (eine Zahl)
    aktuelle_preiskarte = preiskarten.pop()
    print("Gezogen wurde die Preiskarte", aktuelle_preiskarte)
    # Auswahl der Karten von Spieler 1 und Spieler 2 
    # -> Ich habe spieler1_karte und spieler2_karte, beides sind Zahlen
    spieler1_karte = spieler1_kartenspiel.pop()
    while True:
        spieler2_karte = aktuelle_preiskarte + random.randint(-1,1)
        if aktuelle_preiskarte in spieler2_kartenspiel:
            spieler2_kartenspiel.remove(aktuelle_preiskarte)
            break
        


    print("Spieler 1 spielt eine {}, Spieler 2 spielt eine {}".format(\
        spieler1_karte, spieler2_karte))

    # Vergleich der Wertigkeit der Karten
    # Falls spieler1_karte>spieler2_karte: 
    # ## erhöhe spieler1_punkte um preiskarte
    if spieler1_karte>spieler2_karte:
        spieler1_punkte += aktuelle_preiskarte
        print("Spieler 1 gewinnt die Runde!")
    # sonst falls spieler2_karte>spieler1_karte:
    # ## erhöhe spieler2_punkte um preiskarte
    elif spieler2_karte>spieler1_karte:
        spieler2_punkte += aktuelle_preiskarte
        print("Spieler 2 gewinnt die Runde!")
    else:
        # sonst Keine bekommt Punkte
        print("Unentschieden!")
    

    print("Es steht {p_sp1} zu {p_sp2}".format(p_sp1 = spieler1_punkte, p_sp2 = spieler2_punkte))





# Ab hier: FERTIG!
# Spielende - Auswertung (möglicherweise: Neustart)
#print(spieler1_punkte, ":", spieler2_punkte)
print("Es steht {p_sp1} zu {p_sp2}".format(p_sp1 = spieler1_punkte, p_sp2 = spieler2_punkte))
if spieler1_punkte>spieler2_punkte:
    print("Spieler 1 hat gewonnen!")
elif spieler1_punkte<spieler2_punkte:
    print("Spieler 2 hat gewonnen!")
else:
    print("Unentschieden!")