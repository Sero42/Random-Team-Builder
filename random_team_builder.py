import random
import sys

def Einzelnamen(list_of_names, sampling):
    for c in range(len(list_of_names)):
      print(sampling[c])
      print('Darf es noch ein Name sein (1), oder möchtest Du das Programm beenden (2)?')
      Entscheidung = input()
      if Entscheidung == 1:
          Einzelnamen(list_of_names, sampling)
      if Entscheidung == '2':
          print('Möchtest du den Stand bis jetzt speichern (1), die ganze Liste speichern (2) oder einfach nur beenden (3)?')
          endwunsch = input()
          if endwunsch == '1':
              f = open(str(klasse) + "einzel.txt", "w")
              f.write(str(sampling[(c + 1):(len(list_of_names))]))
              f.close()
              sys.exit()
          if endwunsch == '2':
              f = open(str(klasse) + "einzel.txt", "w")
              f.write(str(sampling))
              f.close()
              sys.exit()
          if endwunsch == '3':
              sys.exit()

def alte_Einzelnamen():
    with open(str(klasse) + 'einzel.txt', 'r') as f:
        altes_sample = f.read()
        altes_sample = altes_sample.replace("[", "")
        altes_sample = altes_sample.replace("]", "")
        altes_sample = altes_sample.replace("'", "")
        altes_sample = altes_sample.split(",")
    for c in range(len(altes_sample)):
      print(altes_sample[c])
      print('Darf es noch ein Name sein (1), oder möchtest Du das Programm beenden (2)?')
      Entscheidung = input()
      if Entscheidung == 1:
          alte_Einzelnamen()
      if Entscheidung == '2':
          print('Möchtest du den Stand bis jetzt speichern (1), den vorherigen Stand speichern (2) oder einfach nur beenden (3)?')
          endwunsch = input()
          if endwunsch == '1':
              f = open(str(klasse) + "einzel.txt", "w")
              f.write(str(altes_sample[(c + 1):(len(altes_sample))]))
              f.close()
              sys.exit()
          if endwunsch == '2':
              f = open(str(klasse) + "einzel.txt", "w")
              f.write(str(altes_sample))
              f.close()
              sys.exit()
          if endwunsch == '3':
              sys.exit()

def alte_Gruppen():
    with open(str(klasse) + 'gruppen.txt', 'r') as file:
        for line in file:
            print(line)
    input()
    sys.exit()

def gruppenEnde(dicts):
    print('Möchtest du die Gruppen speichern (1) oder einfach nur beenden (2)?')
    beendigungsart = input()
    if beendigungsart == '1':
        f = open(str(klasse) + "gruppen.txt", "w")
        f.write(str('\n'.join("{}: {}".format(k, v) for k, v in dicts.items())))
        f.close()
        sys.exit()
    else:
        sys.exit()




print('Um welche Klasse geht es?')
klasse = input().lower()

list_of_names = open(str(klasse) + '.txt', encoding='utf-8').read().splitlines()

sampling = random.sample(list_of_names, k=len(list_of_names))


print('Moechtest du Einzelnamen (1) oder Gruppen (2) angezeigt bekommen?')
einzelnamen_oder_gruppen = input()

if einzelnamen_oder_gruppen == '1':
    print('Soll neu begonnen (1) oder fortgesetzt (2) werden?')
    neu_oder_fortgesetzt = input()
    if neu_oder_fortgesetzt == '1':
        Einzelnamen(list_of_names, sampling)
    else:
        alte_Einzelnamen()

else:
    print('Neue Gruppen (1), oder die vom letzten Mal (2)?')
    neue_oder_alte_Gruppen = input()
    if neue_oder_alte_Gruppen == '1':
        print('Wie viele Gruppen sollen es sein?')
        Gruppenanzahl = input()
    else:
        alte_Gruppen()

dicts = {}

anzahl_rest = len(list_of_names) % int(Gruppenanzahl) # anzahl_rest ist die Zahl an Schülern, die beim ganzzahligen
# Teilen von Gesamtschülerzahl durch Gruppenzahl übrigbleibt.

for i in range((anzahl_rest )): # das sind hier die Gruppen, die einen zusätzlichen Schüler bekommen
    c = (i+1) + (i + 1) * (len(list_of_names) // int(Gruppenanzahl))  # c ist die obere Schranke der Gruppen mit einem
    # zusätzlichen Schüler. Für Gruppe 0 (i=0) ergibt sich: 0 + 1 * (Gesamtschülerzahl/Gesamtgruppenzahl (Bsp. 30/4=7) =
    # 7
    d = i + i * (len(list_of_names) // int(Gruppenanzahl)) # d ist die untere Schranke der Gruppen mit einem zusätzlichen
    # Schüler. Bsp. i=0, 30/4: 0 + 0*7 = 0
    dicts[i] = sampling[d:c] # Werte zum Schlüssel i. Im Beispiel i=0 sind es die Schüler zwischen 0 und 7, für i=1 dann
    # zwischen 8 und 16 usw.

for i in range((anzahl_rest), int(Gruppenanzahl)): # Groups without additive student
    c = anzahl_rest + (i + 1) * (len(list_of_names) // int(Gruppenanzahl)) # c ist die obere Schranke Gruppen
    # Für Gruppe 2 (i=2) ergibt sich: 2 + (2+1) * (Gesamtschülerzahl/Gesamtgruppenzahl (Bsp. 30/4=7) =
    # 23
    d = anzahl_rest + i * (len(list_of_names) // int(Gruppenanzahl)) # d ist die untere Schranke
    # Bsp. i=2, 30/4: 2 + 2*7 = 16
    dicts[i] = sampling[d:c] # für 30/4 und i = 2 sind das die Schüler 16 bis 23

print('\n'.join("{}: {}".format(k, v) for k, v in dicts.items()))

gruppenEnde(dicts)






