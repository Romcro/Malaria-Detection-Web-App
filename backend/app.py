from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os

# Importation de CORS avant de l'utiliser
from flask_cors import CORS

# Initialiser l'application Flask
app = Flask(__name__)
CORS(app)  # Permet les requêtes CORS, ce qui est nécessaire pour communiquer entre le frontend (port 3000) et le backend (port 5001)

# Chemin vers le modèle
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'models', 'malaria_model.h5')

# Charger le modèle
print("Chargement du modèle...")
model = tf.keras.models.load_model(MODEL_PATH)
print("Modèle chargé avec succès !")

# Fonction pour préparer l'image pour le modèle
def preprocess_image(image_bytes):
    """
    Prétraite une image pour l'entrée dans le modèle.
    :param image_bytes: Bytes de l'image à traiter.
    :return: Image prétraitée pour le modèle.
    """
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    image = image.resize((64, 64))  # Redimensionner pour correspondre à l'entrée du modèle
    image = np.array(image) / 255.0  # Normaliser les pixels
    image = np.expand_dims(image, axis=0)  # Ajouter une dimension batch
    return image

# Route pour vérifier si le serveur fonctionne
@app.route('/')
def index():
    return "L'API Malaria Detection fonctionne correctement !"

# Route pour effectuer des prédictions
@app.route('/predict', methods=['POST'])
def predict():
    """
    Effectue une prédiction sur une image fournie.
    """
    if 'file' not in request.files:
        return jsonify({"error": "Aucun fichier envoyé"}), 400

    file = request.files['file']
    
    try:
        # Prétraiter l'image
        image = preprocess_image(file.read())
        
        # Faire une prédiction
        prediction = model.predict(image)
        
        # Inversion des prédictions : vous avez inversé "Infecté" et "Non infecté"
        result = "Non infecté" if prediction[0][0] > 0.5 else "Infecté"
        confidence = float(prediction[0][0]) if result == "Infecté" else float(1 - prediction[0][0])

        return jsonify({
            "prediction": result,
            "confidence": confidence
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Lancer le serveur Flask
    app.run(host='0.0.0.0', port=5001, debug=True)
