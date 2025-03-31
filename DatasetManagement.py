import os
import random
import shutil

# def split_images():
#     # Chemins des dossiers
#     train_dir = "FDD_small/train/images"
#     valid_dir = "FDD_small/valid/images"
#     test_dir = "FDD_small/test/images"

#     # Création des dossiers valid et test s'ils n'existent pas
#     os.makedirs(valid_dir, exist_ok=True)
#     os.makedirs(test_dir, exist_ok=True)

#     # Liste des fichiers dans le dossier train/images
#     images = [f for f in os.listdir(train_dir) if os.path.isfile(os.path.join(train_dir, f))]

#     # Sélection de 30% des images
#     sample_size = int(len(images) * 0.3)
#     sampled_images = random.sample(images, sample_size)

#     # Division en deux groupes : 50% pour valid et 50% pour test
#     half_size = len(sampled_images) // 2
#     valid_images = sampled_images[:half_size]
#     test_images = sampled_images[half_size:]

#     # Déplacement des images dans les dossiers correspondants
#     for image in valid_images:
#         shutil.move(os.path.join(train_dir, image), os.path.join(valid_dir, image))

#     for image in test_images:
#         shutil.move(os.path.join(train_dir, image), os.path.join(test_dir, image))

#     print(f"{len(valid_images)} images déplacées vers {valid_dir}")
#     print(f"{len(test_images)} images déplacées vers {test_dir}")

# if __name__ == "__main__":
#     split_images()

def move_labels():
    # Chemins des dossiers
    valid_images_dir = "FDD_small/test/images"
    train_labels_dir = "FDD_small/train/labels"
    valid_labels_dir = "FDD_small/test/labels"

    # Création du dossier valid/labels s'il n'existe pas
    os.makedirs(valid_labels_dir, exist_ok=True)

    # Liste des noms des images dans valid/images (sans extension)
    image_names = [os.path.splitext(f)[0] for f in os.listdir(valid_images_dir) if os.path.isfile(os.path.join(valid_images_dir, f))]

    # Parcours des noms et déplacement des fichiers texte correspondants
    for name in image_names:
        label_file = f"{name}.txt"
        source_path = os.path.join(train_labels_dir, label_file)
        destination_path = os.path.join(valid_labels_dir, label_file)

        # Vérifie si le fichier texte existe avant de le déplacer
        if os.path.exists(source_path):
            shutil.move(source_path, destination_path)
            print(f"Fichier {label_file} déplacé vers {valid_labels_dir}")
        else:
            print(f"Fichier {label_file} introuvable dans {train_labels_dir}")

if __name__ == "__main__":
    move_labels()