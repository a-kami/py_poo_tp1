from article import Article

articles = [
    Article("REF001", "Ordinateur portable", 800.0, 5),
    Article("REF002", "Souris USB", 15.5, 20),
    Article("REF003", "Clavier mécanique", 75.0, 8)
]

# Affichage des articles
for article in articles:
    print(article)

# Calcul de la valeur totale
total = sum(a.valeur_stock() for a in articles)
print(f"Valeur d'inventaire : {total:.2f} €")

# Approvisionner certains articles
articles[0].approvisionner(3)  # +3 ordinateurs
articles[1].approvisionner(10) # +10 souris


print("\n\nAPRÈS approvisionnement:")
for article in articles:
    print(article)

# Calculer la valeur totale APRÈS
total_apres = sum(a.valeur_stock() for a in articles)
print(f"Valeur d'inventaire : {total_apres:.2f} €")