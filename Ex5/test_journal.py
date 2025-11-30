from journal import JournalTaches
from time import sleep

# Écrire dans le journal
with JournalTaches() as journal:
    journal.enregistrer("Préparer la réunion du projet X")
    sleep(1)
    journal.enregistrer("Faire la revue de code")
    sleep(1)
    journal.enregistrer("Envoyer le rapport hebdomadaire")

# Lire le journal (optionnel)
print("Contenu du journal (ordre inverse):")
JournalTaches.lire()
