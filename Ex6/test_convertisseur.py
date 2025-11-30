from convertisseur import Convertisseur

montant = 100
print("Avant mise à jour :", Convertisseur.vers_dh(montant))

Convertisseur.mettre_a_jour_taux(11.2)
print("Après mise à jour  :", Convertisseur.vers_dh(montant))

# Test conversion inverse
dirhams = 1120
print(f"{dirhams} DH = {Convertisseur.vers_eur(dirhams):.2f} EUR")