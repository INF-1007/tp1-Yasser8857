
import math

try:
   Longueur=float(input("Entrez la longueur horizontale (en metres) : ")) 
   if Longueur<=0:
    print("Erreur - donnees invalides.")
    quit()
except ValueError:
    print("Erreur - donnees invalides.")
try:
   Hauteur=float(input("Entrez la hauteur a franchir (en centimetres) : "))
   if Hauteur<0:
    print("Erreur - donnees invalides.")
    quit()
except ValueError:
    print("Erreur - donnees invalides.")

Hauteur_m= Hauteur / 100
pente = (Hauteur_m/ Longueur) * 100
angle =  math.degrees(math.atan(Hauteur_m / Longueur))

if pente>8:
 Conforme="NON"
 Depassement=(pente-8.00)
else :
 Conforme="OUI"

print(f"Pente: {pente:0>5.2f}%")
print(f"Angle:{angle:0>5.2f} deg")
print(f"Conforme : {Conforme}")
if Conforme=="NON":
 print(f"Dépassement:{Depassement:0>5.2f}%")
   
