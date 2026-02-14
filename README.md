# 🖼️ Py Black Out

Un script Python 🐍 utilisant OpenCV 👁️ pour recadrer automatiquement des images et générer un fichier ZIP 📦.

## 📖 Description

Ce projet permet de traiter automatiquement un ensemble d’images 📸 en appliquant :

- conversion en niveaux de gris 🎨
- binarisation automatique (Otsu) ⚡
- détection du contour principal ✂️
- recadrage intelligent de l’objet principal 🎯
- sauvegarde des images traitées dans un dossier de sortie 💾
- création automatique d’un fichier ZIP final 📦

## ⚙️ Installation

### 📥 Cloner le projet

```bash
git clone https://github.com/biyayinux/py-black-out.git
```

### 📂 Accéder au dossier

```bash
cd py-black-out
```

### 🐍 Installer les dépendances

```bash
pip install -r requirements.txt
```

## ▶️ Utilisation

### 📂 Ajouter vos images

Placez vos fichiers `.png`, `.jpg`, ou `.jpeg` dans le dossier :

```bash
images_input/
```

### 🚀 Lancer le script

```bash
python src/main.py
```

## ✅ Résultat

Les images recadrées seront enregistrées dans :

📁 `images_output/`

Un fichier ZIP sera automatiquement généré :

📦 `resultat_images.zip`

## ⚠️ Problèmes connus

- Le script ignore les fichiers non valides ❌
- Fonctionne uniquement avec des images contenant un objet détectable 📸

## 📜 Licence

Vous êtes libre d’utilisation pour l’apprentissage et le traitement d’images avec OpenCV 👁️.
