class Article:

    def __init__(self, reference: str, designation: str, prix_ht: float, stock: int = 0):
        self.reference = reference
        self.designation = designation
        self.prix_ht = prix_ht
        self.stock = stock

    def valeur_stock(self) -> float:
        return self.prix_ht * self.stock

    def approvisionner(self, qte: int):
        self.stock += qte
        with open("mouvements.log", "a") as f:
            f.write(f"Approvisionnement: {qte} unités de {self.reference} - Nouveau stock: {self.stock}\n")

    def __str__(self):
        return f"Réf {self.reference} — {self.designation} : {self.stock} unités à {self.prix_ht} € HT"