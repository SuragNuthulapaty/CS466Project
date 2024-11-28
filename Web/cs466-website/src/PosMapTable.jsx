import React from "react";
import { Grid, Paper, Typography, Box } from "@mui/material";

const posMap = {
  "Adjective": "A",
  "Adposition": "P",
  "Adverb": "R",
  "Auxiliary Verb": "X",
  "Coordinating Conjunction": "C",
  "Determiner": "D",
  "Interjection": "I",
  "Noun": "N",
  "Numeral": "M",
  "Particle": "T",
  "Pronoun": "O",
  "Proper Noun": "P",
  "Punctuation": "U",
  "Subordinating Conjunction": "S",
  "Symbol": "Y",
  "Verb": "V",
  "Other": "X",
  "Whitespace": "E",
};

const posMapData = Object.entries(posMap).map(([posName, abbreviation]) => ({
  posName,
  abbreviation,
}));

const PosMapGrid = () => {
  return (
    <Box
      sx={{
        padding: 4,
        margin: "20px auto",
        maxWidth: 800,
        textAlign: "center",
      }}
    >
      <Typography
        variant="h5"
        sx={{ marginBottom: 2, color: "#4CAF50", fontWeight: "bold" }}
      >
        Part of Speech Mapping
      </Typography>
      <Grid container spacing={2}>
        {posMapData.map((row, index) => (
          <Grid item xs={2} key={index} sx={{ display: "flex", flexDirection: "column" }}>
            <Paper
              elevation={3}
              sx={{
                display: "flex",
                flexDirection: "column",
                justifyContent: "center",
                alignItems: "center",
                padding: 2,
                textAlign: "center",
                backgroundColor: "#f9f9f9",
                border: "1px solid #ddd",
                height: "100%"
              }}
            >
              <Typography variant="subtitle1" fontWeight="bold">
                {row.posName}
              </Typography>
              <Typography variant="subtitle2" color="textSecondary">
                {row.abbreviation}
              </Typography>
            </Paper>
          </Grid>
        ))}
      </Grid>
    </Box>
  );
};

export default PosMapGrid;
