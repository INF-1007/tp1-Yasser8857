Personnes=[]
FACTEURS = [1.30, 1.15, 1.05, 0.95, 0.95, 1.05, 1.15, 1.30]

for k in range(8):
    try:
        nb_de_personnes = int(input("Entrez le nombre de personnes : "))
        if nb_de_personnes < 0:
            print("Erreur - donnees invalides.")
            quit()
        Personnes.append(nb_de_personnes)
    except ValueError:
        print("Erreur - donnees invalides.")
        quit()

Intensités=[(P*F) for P,F in zip(Personnes, FACTEURS)]
maxI=max(Intensités)
if maxI==0:
 niveaux=[0]*8
else: niveaux= [int((n / maxI) * 10 + 0.5) for n in Intensités]
 
 

for niveau_ligne in range(10,0,-1):
 cellules=[]
 for niveau_section in niveaux :
    if niveau_section>= niveau_ligne:
     cellules.append("❚"+" ")
    else:
     cellules.append("."+" ")
 print(f'{niveau_ligne:>2d}|'+ "".join(cellules))
print("   A B C D E F G H")


