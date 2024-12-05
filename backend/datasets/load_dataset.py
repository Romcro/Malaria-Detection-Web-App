import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt

def load_and_preprocess_dataset():
    """Charge et prétraite le dataset Malaria."""
    # Charger les données depuis TensorFlow Datasets
    ds, ds_info = tfds.load('malaria', as_supervised=True, with_info=True)

    # Fonction de prétraitement
    def preprocess(image, label):
        image = tf.image.resize(image, (64, 64))  # Redimensionner les images
        image = tf.cast(image, tf.float32) / 255.0  # Normaliser les images
        return image, label

    # Récupérer tout l'ensemble
    ds_all = ds['train'].map(preprocess)

    # Obtenir la taille du dataset
    dataset_size = tf.data.experimental.cardinality(ds_all).numpy()
    train_size = int(0.8 * dataset_size)

    # Diviser en entraînement et test (80% train, 20% test)
    ds_all = ds_all.shuffle(10000)  # Mélanger les données
    ds_train = ds_all.take(train_size).batch(32)
    ds_test = ds_all.skip(train_size).batch(32)

    return ds_train, ds_test, ds_info

def plot_samples(dataset, num_samples=20):
    """Affiche quelques exemples d'images du dataset."""
    plt.figure(figsize=(20, 10))
    for i, (images, labels) in enumerate(dataset.take(1)):  # Prendre un batch
        for j in range(min(num_samples, len(images))):  # Limiter au nombre d'images disponibles
            ax = plt.subplot(4, 5, j + 1)  # Disposition des images sur 4 lignes, 5 colonnes
            plt.imshow(images[j].numpy())  # Afficher une image individuelle
            plt.title("Infected" if labels[j].numpy() == 0 else "Uninfected")  # Label 0 = Infecté
            plt.axis("off")
        break
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Test du chargement et de l'exploration
    ds_train, ds_test, ds_info = load_and_preprocess_dataset()
    print(ds_info)  # Informations générales sur le dataset
    plot_samples(ds_train)  # Afficher quelques exemples
