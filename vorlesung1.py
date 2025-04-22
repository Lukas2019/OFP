from random import random


def print_cards(karten_liste):
    for i, karte in enumerate(karten_liste):
        print (str(i)+ ": " + karte)


def karte_ziehen():
    return werte[int(random() * 12)] + " " + farben[int(random() * 4)]


def gewinn_spieler1(karte1, karte2):
    # Punkte für jede Karte definieren
    punkte = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
        "Bube": 11, "Dame": 12, "König": 13, "Ass": 14
        }

    bridge_farbwert = {"Pik": 4, "Herz": 3, "Karo": 2, "Kreuz": 1}

    karte1_split = karte1.split(" ")
    karte2_split = karte2.split(" ")

    if punkte[karte1_split[0]]>punkte[karte2_split[0]]:
        return True
    elif punkte[karte1_split[0]]==punkte[karte2_split[0]]:
        if bridge_farbwert[karte1_split[1]]>bridge_farbwert[karte2_split[1]]:
            return True
    return False


def punkte(karten):
    punkte_tabelle = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
        "Bube": 11, "Dame": 12, "König": 13, "Ass": 14
        }
    punkte = 0
    for karte in karten:
        karte_split = karte.split(" ")
        punkte += punkte_tabelle[karte_split[0]]
    return punkte
    

# Definiere die Farben und die Kartenwerte
farben = ["Kreuz", "Pik", "Herz", "Karo"]
werte = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube", "Dame", "König", "Ass"]

# Karten verteilen

verteilte_karten = []

karten_sp1 = []
gewonne_karte_sp1 = []
karten_sp2 = []
gewonne_karte_sp2 = []

while len(karten_sp2) < 10:
    karte = karte_ziehen()
    if karte not in verteilte_karten:
        verteilte_karten.append(karte)
        if len(karten_sp1) < 10:
            karten_sp1.append(karte)
        elif len(karten_sp2)<10:
            karten_sp2.append(karte)

while karten_sp1:
    # Spiel
    karte_gezogen = False
    while not karte_gezogen:
        karte = karte_ziehen()
        if karte not in verteilte_karten:
            verteilte_karten.append(karte)
            karte_gezogen=karte

    print("Deine Karten:")

    print_cards(karten_sp1)

    gewählte_karte_sp1= int(input("Wähle eine Karte:"))

    print_cards(karten_sp2)

    gewählte_karte_sp2 = int(input("Wähle eine Karte:"))

    ## Gewinner Kalkulieren

    if gewinn_spieler1(karten_sp1[gewählte_karte_sp1], karten_sp2[gewählte_karte_sp2]):
        gewonne_karte_sp1.append(karte_gezogen)
        print(f"Spieler 1 gewinnt {karten_sp1[gewählte_karte_sp1]}.")
    else:
        gewonne_karte_sp2.append(karte_gezogen)
        print(f"Spieler 2 gewinnt {karte_gezogen}.")

    karten_sp1.pop(gewählte_karte_sp1)
    karten_sp2.pop(gewählte_karte_sp2)

punkte_sp1 = punkte(gewonne_karte_sp1)
punkte_sp2 = punkte(gewonne_karte_sp2)

if punkte_sp2 == punkte_sp1:
    print(f"Unentschieden mit {punkte_sp1} Punkten.")
elif punkte_sp1 > punkte_sp2:
    print(f"Spieler 1 gwinnt mit {punkte_sp1}")
else:
    print(f"Spieler 2 gwinnt mit {punkte_sp2} Punkten.")
