import math

prompts = [
    "Entrez la distance jusqu'au CEPSUM (en kilometres) : ",
    "Entrez le temps d'attente de la navette (en minutes) : ",
    "Entrez le temps du trajet en metro (en minutes) : ",
    "Entrez le temps de controle a l'entree (en minutes) : "
]

valeurs = []

for message in prompts:
    try:
        Mesure = float(input(message))
        if Mesure < 0:
            print("Erreur - donnees invalides.")
            quit()
        valeurs.append(Mesure)
    except ValueError:
        print("Erreur - donnees invalides.")
        quit()

distance,attente_navette,temps_metro,controle= valeurs
marche = distance * 60 / 5 + controle
navette = attente_navette + distance * 60 / 18 + controle
metro   = temps_metro + controle

for c in (marche,navette,metro):
    math.ceil(c)
OPTIONS=[("marcher",marche),("navette",navette),("metro",metro)]
minimum=min(marche,navette,metro)
Vainqueurs=[mot for mot,réponse in OPTIONS if réponse==minimum]
if len(Vainqueurs)==1:
  print(f"Option la plus rapide :{Vainqueurs[0]}")
elif len (Vainqueurs)==2:
 print(f"Égalité:{Vainqueurs[0]} et {Vainqueurs[1]}")
else:
  print("Egalite : marcher, navette et metro.")
