from datetime import datetime

class JournalTaches:
    def __enter__(self):
        self.fichier = open("journal.txt", "a", encoding="UTF-8")
        return self
    
    def enregistrer(self, tache: str):
        date_heure = datetime.now().isoformat()
        self.fichier.write(f"{date_heure} - {tache}\n")
    
    def __exit__(self, exc_type, exc, tb):
        self.fichier.close()
    
    @classmethod
    def lire(cls):
        try:
            with open("journal.txt", "r", encoding="UTF-8") as f:
                lignes = f.readlines()
                for ligne in reversed(lignes):
                    print(ligne.strip())
        except FileNotFoundError:
            print("Aucun journal trouvé")