
try: 
 nom_complet=input( "Entrez votre nom complet : ")
except ValueError:
    print("Erreur - donnees invalides.")
try: 
 matchs_football=int(input( "Entrez le nombre de matchs de football des Carabins suivis cet automne : "))
except ValueError:
          print("Erreur - donnees invalides.")
try:
 durée_football=int(input("Entrez la duree moyenne d'un match de football suivi (en minutes) : "))
except ValueError:
        print("Erreur - donnees invalides.")

try:
 matchs_soccer=int(input("(Entrez le nombre de matchs de soccer feminin des Carabins suivis cet automne :"))
except ValueError:
               print("Erreur - donnees invalides.")

try:
 durée_soccer=int(input("Entrez la duree moyenne d'un match de soccer suivi (en minutes) : "))
except ValueError:
       print("Erreur - donnees invalides.")


if (matchs_football and matchs_soccer) <0: 
        print("Erreur - donnees invalides.")

if(durée_soccer and durée_football)<=0:
  print("Erreur - donnees invalides.")

minutes_soccer=f"{(durée_soccer)//60}:{(durée_soccer%60):02d}"
minutes_football=f"{(durée_football)//60}:{(durée_football%60):02d}"
total=durée_football+durée_soccer
total=(f"{total//60}:{total%60:02d}")

print(f"""Bonjour {nom_complet}
    Football (Carabins): {matchs_football} match(s), {minutes_football} de visionnage
    Soccer (Carabins): {matchs_soccer} match(s), {minutes_soccer} de visionnage
    Total: {total}""")

