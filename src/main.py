import cv2
import os
import shutil

# Dossiers d'entrée et de sortie
input_folder = "images_input"
output_folder = "images_output"
os.makedirs(output_folder, exist_ok=True)

# Parcourir les fichiers du dossier
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        img = cv2.imread(os.path.join(input_folder, filename))
        if img is None: continue

        # Traitement OpenCV
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            p = 2
            cropped = img[y+p : y+h-p, x+p : x+w-p]
            
            # Sauvegarde dans le dossier de sortie
            cv2.imwrite(os.path.join(output_folder, filename), cropped)

print("Traitement des images terminé")

# Création du fichier ZIP
shutil.make_archive("resultat_images", 'zip', output_folder)
print("Fichier resultat_images.zip créé avec succès")
