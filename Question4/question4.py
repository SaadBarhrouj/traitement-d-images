# Importation des bibliothèques nécessaires 
from matplotlib import pyplot as plt  # Pour générer l'histogramme
import numpy as np  # Pour manipuler les matrices
from PIL import Image  # Pour ouvrir et manipuler des images
from os import path  # Pour vérifier l'existence de l'image

# Demander à l'utilisateur de saisir le chemin complet de l'image
print("Entrez le chemin d'accès complet de l'image (par exemple, /chemin/vers/image.jpg) : ")
nom_image = input()

# Vérifier si le fichier existe
if not path.exists(nom_image):
    print("Image introuvable !")
    exit()

# Ouvrir l'image
image = Image.open(nom_image)

# Conversion de l'image en niveaux de gris si elle ne l'est pas déjà
if image.mode != 'L':
    image = image.convert('L')

# Récupérer les pixels de l'image sous forme de liste
pixels = list(image.getdata())

# Convertir la liste de pixels en un tableau NumPy
pixels_array = np.array(pixels)

# Générer l'histogramme avec 255 bins (pour chaque niveau de gris de 0 à 255)
plt.hist(pixels_array, bins=255, color='gray', edgecolor='black')

# Ajouter un titre en français
plt.title("Histogramme des niveaux de gris")

# Afficher l'histogramme
plt.show()
