# Flouter les visages sur vos photos et vidéos

Un outil simple et gratuit pour flouter automatiquement les visages sur vos photos et vidéos (manifestations, événements, etc.), **sans aucune connaissance technique**.

Il utilise [Deface](https://github.com/ORB-HD/deface) et fonctionne entièrement sur votre ordinateur : **vos fichiers ne sont envoyés nulle part**.

---

## Ce qu'il faut savoir avant de commencer

- Vous n'avez besoin de taper **aucune commande**, il suffit de double-cliquer.
- Vos fichiers originaux ne sont **jamais modifiés** : les versions floutées sont créées à côté.
- ⚠️ **Aucun outil automatique n'est fiable à 100 %.** Vérifiez toujours le résultat avant de publier (voir plus bas).

---

## Étape 1 : Installer Python (une seule fois)

### Windows
1. Allez sur https://www.python.org/downloads/
2. Cliquez sur le gros bouton jaune pour télécharger.
3. Lancez le fichier téléchargé.
4. **IMPORTANT : cochez la case « Add Python to PATH »** en bas de la fenêtre, puis cliquez sur **Install Now**.

### Mac
Téléchargez l'installateur sur https://www.python.org/downloads/ et installez-le comme n'importe quelle application.

### Linux
Python est généralement déjà installé. Sinon : `sudo apt install python3 python3-pip`

---

## Étape 2 : Télécharger l'outil

1. En haut de cette page, cliquez sur le bouton vert **Code**.
2. Cliquez sur **Download ZIP**.
3. Faites un clic droit sur le fichier ZIP téléchargé puis **Extraire tout** (ou « Décompresser »).

---

## Étape 3 : Mettre vos fichiers

Dans le dossier décompressé, créez un dossier nommé exactement :

```
A_FLOUTER
```

(Il sera aussi créé automatiquement au premier lancement.)

Copiez-y vos photos et vidéos. Formats acceptés : `.jpg` `.jpeg` `.png` `.mp4` `.mov` `.avi` `.mkv`

---

## Étape 4 : Lancer

### Windows
Double-cliquez sur **`LANCER_WINDOWS.bat`**

> Si Windows affiche « Windows a protégé votre ordinateur » : cliquez sur **Informations complémentaires** puis **Exécuter quand même**. Le fichier ne fait que lancer le script visible dans ce dépôt, vous pouvez l'ouvrir avec le Bloc-notes pour vérifier.

### Mac / Linux
Ouvrez un terminal dans le dossier et tapez :

```
python3 flouter.py
```

(Pour la toute première utilisation, tapez d'abord `pip3 install deface`.)

Une fenêtre noire s'ouvre et affiche l'avancement. **C'est normal**, laissez-la travailler. La première fois, l'installation peut prendre quelques minutes. Les vidéos peuvent être longues à traiter, surtout sans carte graphique : soyez patient.

---

## Étape 5 : Récupérer le résultat

Vos fichiers floutés sont dans le dossier **`FLOUTE`**, avec le préfixe `floute_`.

Les visages sont masqués par un **aplat noir** (plus sûr qu'un flou, qui peut parfois être « défloué »).

---

## ⚠️ Étape 6 : VÉRIFIER avant de publier (indispensable)

Le logiciel peut rater des visages. Avant de publier :

- Regardez **chaque image** attentivement.
- Pour les **vidéos**, regardez-les **en entier** : un visage non détecté sur quelques secondes suffit à identifier quelqu'un.
- Faites attention aux visages **de profil, petits, dans l'ombre, flous, partiellement cachés**.
- Si un visage est resté visible, masquez-le à la main avec un éditeur gratuit : [GIMP](https://www.gimp.org/) (photos) ou [Shotcut](https://shotcut.org/) / [Kdenlive](https://kdenlive.org/) (vidéos).

---

## Ne pas oublier : d'autres éléments identifient

Flouter le visage ne suffit pas toujours. Pensez à masquer aussi :

- Tatouages, cicatrices, vêtements ou sacs très distinctifs
- Plaques d'immatriculation
- Badges, noms sur les vêtements, pancartes personnelles

### Les métadonnées

Vos photos et vidéos contiennent des informations cachées (position GPS, modèle de téléphone, date et heure). **Le floutage ne les supprime pas.**

- **Windows** : clic droit sur le fichier, **Propriétés**, onglet **Détails**, puis **Supprimer les propriétés et les informations personnelles**.
- **Mac / Linux** : avec l'outil `exiftool`, tapez `exiftool -all= mon_fichier.jpg`

Astuce : une capture d'écran de votre photo ne contient pas les métadonnées d'origine.

---

## Problèmes courants

| Problème | Solution |
|---|---|
| « python n'est pas reconnu » | Réinstallez Python en cochant **Add Python to PATH**, puis relancez |
| Rien ne se passe / fenêtre qui se ferme | Vérifiez que vos fichiers sont bien dans `A_FLOUTER` |
| Très lent sur les vidéos | Normal sans carte graphique. Patientez ou découpez la vidéo en morceaux |
| Des visages sont ratés | Voir étape 6 (masquage manuel) |

---

## Pour les utilisateurs avancés

Le script utilise ces réglages, modifiables dans `flouter.py` :

- `--thresh 0.2` : sensibilité de détection (plus bas = détecte plus de visages, avec quelques faux positifs)
- `--mask-scale 1.5` : taille de la zone masquée
- `--replacewith solid` : aplat noir (autres options : `blur`, `mosaic`)

Pour plus d'options, voir la [documentation de Deface](https://github.com/ORB-HD/deface).

---

Prenez soin de vous et des autres. 🖤

## Contribuer

Ce projet est libre (licence MIT) : vous pouvez le copier, le modifier, l'améliorer et le partager.
Une idée, un bug, une traduction ? Ouvrez une « Issue » ou proposez une « Pull request ».
