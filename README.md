Voici le `README.md` mis à jour en tenant compte des modifications que vous m'avez indiquées, et en retirant la mention de Vue.js et TensorFlow.js, comme demandé :

---

# 🌟 Malaria Detection Web App 🌟

Une application web pour détecter la présence de malaria dans les images de cellules, basée sur un modèle de Deep Learning 🚀.

## 🧐 À propos du projet

Ce projet combine des technologies modernes pour permettre l’analyse automatique d’images de cellules et la détection de malaria :

- **🔬 Modèle Deep Learning** : Un CNN entraîné pour classer les images.
- **🖥️ Front-End** : Développé avec **React**, déployé sur **GitHub Pages**.
- **⚙️ Back-End** :
  - Hébergé sur **Azure App Service** avec une architecture conteneurisée (**Docker**).
  - **Firebase Functions** utilisé comme solution de redondance gratuite pour assurer une haute disponibilité.

## 🛠️ Technologies Utilisées

### 💻 Front-End

- **React** 🖼️
- **HTML, CSS, JavaScript** 🌐

### 📡 Back-End

- **Azure App Services (Docker)** ☁️
- **Firebase Functions** 🔥

### 📊 Machine Learning

- **TensorFlow/Keras** 🎛️
  - Modèle CNN pour la classification des cellules 🧬

## 📋 Fonctionnalités

- **📤 Télécharger une image** : Chargez une image de cellule depuis votre appareil.
- **🔍 Analyse automatique** : Détection instantanée de malaria dans l’image.
- **🛡️ Disponibilité garantie** : Redondance entre Azure et Firebase pour une continuité du service.

## 🚀 Démarrage Rapide

1️⃣ **Cloner le dépôt**

```bash
git clone https://github.com/Romcro/Malaria-Detection-Web-App.git
cd Malaria-Detection-Web-App
```

2️⃣ **Installation des dépendances**

- Pour le front-end (React) :

```bash
cd frontend
npm install
```

- Pour le back-end (Firebase Functions) :

```bash
cd backend/functions
npm install
```

- Pour l’entraînement du modèle (Python) :

```bash
cd backend
python -m venv venv
source venv/bin/activate # (ou venv\Scripts\activate sous Windows)
pip install -r requirements.txt
```

3️⃣ **Lancer l’application**

- **Front-End** :

```bash
cd frontend
npm run serve
```

- **Back-End Dockerisé (Azure)** :

```bash
cd backend
docker build -t malaria-backend .
docker run -p 5000:5000 malaria-backend
```

- **Back-End Firebase** :
  - Déployez les fonctions Firebase :
  ```bash
  firebase deploy --only functions
  ```
  - Ou testez localement :
  ```bash
  firebase emulators:start
  ```

## 🌍 Déploiement

### Front-End

- Déployé sur **GitHub Pages** 🕸️.

### Back-End

- Principal : Hébergé sur **Azure (Dockerisé)** ☁️.
- Secondaire (Redondance) : Hébergé sur **Firebase Functions** 🔥.

## 📂 Structure du Projet

```plaintext
📦 Malaria-Detection-Web-App
├── 📂 frontend         # Code React
│   ├── 📂 public       # Modèles statiques
│   └── 📂 src          # Composants React
├── 📂 backend          # Code Python + API Dockerisée
│   ├── functions       # API Firebase Functions (redondance)
│   ├── app.py          # Code API principal (Flask/FastAPI)
│   ├── Dockerfile      # Configuration Docker pour Azure
│   ├── firebase.json   # Configuration Firebase
│   └── requirements.txt # Dépendances Python
├── 📂 docs             # Documentation technique
├── 📂 data             # Dataset (local uniquement)
├── model.h5            # Modèle TensorFlow (pré-entraînement)
├── README.md           # Ce fichier 📝
```

## 🎯 Objectifs

- **Précision du modèle** : Atteindre au moins 90% sur le dataset de test.
- **Temps de réponse** : Fournir une analyse en moins de 5 secondes.
- **Stabilité** : Garantir une disponibilité continue grâce à la redondance Azure + Firebase.

## 🤝 Contribuer

Les contributions sont les bienvenues ! 🎉

1. Forkez le projet 🍴.
2. Créez une branche (git checkout -b feature/nom-feature) 🌿.
3. Commitez vos changements (git commit -m 'Ajout d'une nouvelle feature') 💬.
4. Poussez sur la branche (git push origin feature/nom-feature) 🚀.
5. Créez une Pull Request 📬.

## 🛡️ Licence

Ce projet est sous **licence MIT**.

## 🧑‍💻 Auteur

Romuald Crochat - [GitHub](https://github.com/Romcro) | [LinkedIn](https://www.linkedin.com/in/romuald-crochat)

⭐ Merci d’utiliser cette application !  
Si vous aimez ce projet, n’hésitez pas à donner une ⭐ sur le dépôt GitHub. 😊

This site is open source. Improve this page.

---
