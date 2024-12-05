import React, { useState } from "react";
import axios from "axios";
import { Button, Typography, Container, Card, Box } from "@mui/material";
import { motion } from "framer-motion";

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      alert("Veuillez sélectionner une image !");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await axios.post("http://localhost:5001/predict", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      setResult(response.data);
    } catch (error) {
      console.error("Erreur lors de la requête :", error);
      alert("Une erreur s'est produite !");
    }
  };

  return (
    <Container style={{ backgroundColor: "#121212", height: "100vh", padding: "20px" }}>
      {/* Titre animé */}
      <motion.div
        initial={{ opacity: 0, y: -50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 1 }}
      >
        <Typography variant="h3" gutterBottom sx={{ textAlign: "center", color: "#fff" }}>
          Détection de Malaria
        </Typography>
      </motion.div>

      <Box sx={{ display: "flex", justifyContent: "center", marginTop: 2 }}>
        {/* Formulaire avec animation d'échelle */}
        <motion.div
          initial={{ scale: 0.8 }}
          animate={{ scale: 1 }}
          transition={{ type: "spring", stiffness: 300 }}
        >
          <Card
            variant="outlined"
            sx={{ padding: 3, width: 350, backgroundColor: "#333" }}
          >
            {/* Animation sur le champ de fichier */}
            <motion.input
              type="file"
              onChange={handleFileChange}
              style={{
                padding: "10px",
                backgroundColor: "#444",
                border: "1px solid #555",
                color: "#fff",
              }}
              whileHover={{ scale: 1.05 }}
            />

            {/* Animation sur le bouton */}
            <motion.button
              whileHover={{ scale: 1.1, backgroundColor: "#007BFF" }}
              whileTap={{ scale: 0.95 }}
              style={{
                marginTop: "20px",
                padding: "10px",
                background: "#007BFF",
                color: "white",
                border: "none",
                borderRadius: "5px",
                cursor: "pointer",
                transition: "background 0.2s ease",
              }}
              onClick={handleUpload}
            >
              Envoyer
            </motion.button>

            {/* Résultat avec animation de transparence */}
            {result && (
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ duration: 0.5 }}
                style={{ marginTop: "20px" }}
              >
                <Typography variant="h6" style={{ color: "#fff" }}>
                  Résultat :
                </Typography>
                <Typography variant="body1" style={{ color: "#ccc" }}>
                  Prédiction : {result.prediction}
                </Typography>
                <Typography variant="body1" style={{ color: "#ccc" }}>
                  Confiance : {result.confidence}
                </Typography>
              </motion.div>
            )}
          </Card>
        </motion.div>
      </Box>
    </Container>
  );
}

export default App;
