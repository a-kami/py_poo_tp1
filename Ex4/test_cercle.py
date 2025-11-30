from cercle import Cercle
from math import pi

c = Cercle(3)
print(f"Périmètre: {c.perimetre:.2f}")  # 2πr
print(f"Surface: {c.surface:.2f}")      # πr²

try:
    c.rayon = -5
except ValueError as e:
    print("Erreur capturée :", e)

# Test agrandir
c.agrandir(50)  # +50%
print(f"Nouveau rayon: {c.rayon}")
print(f"Nouveau périmètre: {c.perimetre:.2f}")