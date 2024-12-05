import sys
import os
import tensorflow as tf
import matplotlib.pyplot as plt

# Ajouter dynamiquement le chemin du dossier 'datasets'
current_dir = os.path.dirname(os.path.abspath(__file__))  # Chemin du fichier actuel
datasets_dir = os.path.join(current_dir, '../datasets')  # Chemin relatif vers 'datasets'
sys.path.append(datasets_dir)

from load_dataset import load_and_preprocess_dataset  # Importer la fonction depuis load_dataset.py

def build_model():
    """Construit un modèle CNN pour la classification binaire."""
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(64, 64, 3)),  # Définir l'entrée
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.5),  # Dropout pour réduire l'overfitting
        tf.keras.layers.Dense(1, activation='sigmoid')  # Sortie binaire
    ])
    return model

def plot_training_history(history, save_dir):
    """Génère et sauvegarde les graphiques d'entraînement."""
    os.makedirs(save_dir, exist_ok=True)  # Crée le dossier s'il n'existe pas

    # Courbe de la précision
    plt.figure(figsize=(8, 6))
    plt.plot(history.history['accuracy'], label='Train Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.title('Training and Validation Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    accuracy_path = os.path.join(save_dir, 'accuracy.png')
    plt.savefig(accuracy_path)
    plt.close()
    print(f"Graphique de précision sauvegardé sous '{accuracy_path}'.")

    # Courbe de la perte
    plt.figure(figsize=(8, 6))
    plt.plot(history.history['loss'], label='Train Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title('Training and Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    loss_path = os.path.join(save_dir, 'loss.png')
    plt.savefig(loss_path)
    plt.close()
    print(f"Graphique de perte sauvegardé sous '{loss_path}'.")

def train_model():
    """Charge les données, construit le modèle, entraîne et sauvegarde le modèle."""
    # Charger les datasets
    ds_train, ds_test, ds_info = load_and_preprocess_dataset()

    # Construire le modèle
    model = build_model()
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    # Entraîner le modèle avec un EarlyStopping
    history = model.fit(
        ds_train,
        validation_data=ds_test,
        epochs=50,  # Nombre maximum d'époques
        callbacks=[
            tf.keras.callbacks.EarlyStopping(
                monitor='val_loss',  # Surveille la perte de validation
                patience=3,  # Stoppe si pas d'amélioration pendant 3 époques
                restore_best_weights=True  # Restaure les meilleurs poids
            )
        ]
    )

    # Créer un dossier 'models' pour sauvegarder les modèles
    models_dir = os.path.join(current_dir, '../models')
    os.makedirs(models_dir, exist_ok=True)  # Crée le dossier s'il n'existe pas

    # Sauvegarder le modèle au format HDF5 et Keras
    h5_path = os.path.join(models_dir, "malaria_model.h5")
    keras_path = os.path.join(models_dir, "malaria_model.keras")
    model.save(h5_path)
    print(f"Modèle sauvegardé sous '{h5_path}'.")
    model.save(keras_path)
    print(f"Modèle sauvegardé sous '{keras_path}'.")

    # Générer les graphiques et les sauvegarder
    docs_training_dir = os.path.join(current_dir, '../docs/training')
    plot_training_history(history, docs_training_dir)

if __name__ == "__main__":
    train_model()
