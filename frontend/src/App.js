import React, { useState } from "react";
import axios from "axios";

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null); // Pour gérer les erreurs
  const [loading, setLoading] = useState(false); // Pour gérer l'état de chargement

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
    setError(null); // Réinitialiser les erreurs si une nouvelle image est sélectionnée
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      alert("Veuillez sélectionner une image !");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    setLoading(true); // Début du chargement
    setError(null); // Réinitialiser les erreurs précédentes
    setResult(null); // Réinitialiser le résultat précédent

    try {
      const response = await axios.post("http://127.0.0.1:5001/predict", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      setResult(response.data); // Stocker le résultat de l'API
    } catch (error) {
      console.error("Erreur lors de la requête :", error);
      if (error.response) {
        // Si l'API retourne une erreur avec un code de statut
        setError(
          `Erreur du serveur : ${error.response.status} - ${error.response.data.error}`
        );
      } else if (error.request) {
        // Si la requête a été envoyée mais qu'aucune réponse n'a été reçue
        setError("Erreur réseau : Impossible de contacter le serveur.");
      } else {
        // Autres erreurs (par exemple, erreur de configuration)
        setError("Une erreur s'est produite : " + error.message);
      }
    } finally {
      setLoading(false); // Fin du chargement
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>Détection de Malaria</h1>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Envoi en cours..." : "Envoyer"}
      </button>

      {error && (
        <div style={{ color: "red", marginTop: "20px" }}>
          <strong>Erreur :</strong> {error}
        </div>
      )}

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h2>Résultat :</h2>
          <p>
            <strong>Prédiction :</strong> {result.prediction}
          </p>
          <p>
            <strong>Confiance :</strong> {result.confidence}
          </p>
        </div>
      )}
    </div>
  );
}

export default App;
