import subprocess
import sys
from pathlib import Path

# Dossiers (créés automatiquement à côté du script)
BASE = Path(__file__).parent
DOSSIER_ENTREE = BASE / "A_FLOUTER"
DOSSIER_SORTIE = BASE / "FLOUTE"

EXTENSIONS = {".jpg", ".jpeg", ".png", ".mp4", ".mov", ".avi", ".mkv"}

def main():
    DOSSIER_ENTREE.mkdir(exist_ok=True)
    DOSSIER_SORTIE.mkdir(exist_ok=True)

    fichiers = [f for f in DOSSIER_ENTREE.iterdir()
                if f.suffix.lower() in EXTENSIONS]

    if not fichiers:
        print("Aucun fichier trouvé.")
        print(f"Mettez vos photos/vidéos dans le dossier : {DOSSIER_ENTREE}")
        input("Appuyez sur Entrée pour fermer...")
        return

    print(f"{len(fichiers)} fichier(s) à traiter...\n")

    for f in fichiers:
        sortie = DOSSIER_SORTIE / f"floute_{f.name}"
        print(f"→ {f.name}")
        subprocess.run([
            sys.executable, "-m", "deface", str(f),
            "--thresh", "0.2",
            "--mask-scale", "1.5",
            "--replacewith", "solid",
            "-o", str(sortie),
        ])

    print("\nTerminé ! Résultats dans le dossier FLOUTE.")
    print("⚠️ VÉRIFIEZ visuellement chaque fichier avant de publier.")
    input("Appuyez sur Entrée pour fermer...")

if __name__ == "__main__":
    main()
