import itertools

try:
    nb_billets = int(input("Entrez le nombre de billets necessaires : "))
    etudiant = input("Entrez le statut etudiant (O/N) : ").upper()
    if nb_billets < 0 or etudiant not in {"O","N"}:
        raise ValueError
except ValueError:
    print("Erreur - donnees invalides.")
    quit()


prix_24b = 66.00
prix_12b = 36.00
prix_5b  = 15.75
prix_uni = 3.60

if etudiant == "O":
    prix_24b *= 0.88
    prix_12b *= 0.88
    prix_5b  *= 0.88


meilleur_cout = float('inf')
meilleure_combo = ()

for forfait_24 in range(nb_billets//24 + 2):
 for forfait_12 in range(nb_billets//12 + 2):
  for forfait_5 in range(nb_billets//5 + 2):
     billets_forfaits = 24*forfait_24 + 12*forfait_12 + 5*forfait_5
     if billets_forfaits >= nb_billets:
        billets_unitaires = max(0, nb_billets - billets_forfaits)
        total_billets = billets_forfaits + billets_unitaires
        prix_total = (prix_24b*forfait_24 + prix_12b*forfait_12 +
        prix_5b*forfait_5 + prix_uni*billets_unitaires)


        if (prix_total < meilleur_cout or
         (prix_total == meilleur_cout and total_billets < sum(meilleure_combo[:4])) or
         (prix_total == meilleur_cout and total_billets == sum(meilleure_combo[:4])
         and billets_unitaires < meilleure_combo[3])):
         meilleur_cout = prix_total
         meilleure_combo = (forfait_24, forfait_12, forfait_5,
         billets_unitaires, total_billets, prix_total)

f24, f12, f5, unit, total, prix = meilleure_combo
print(f"Forfaits de 24 billets - {f24}")
print(f"Forfaits de 12 billets - {f12}")
print(f"Forfaits de 5 billets - {f5}")
print(f"Billets unitaires - {unit}")
print(f"Total billets - {total}")
print(f"Prix total - {prix:.2f}$")

