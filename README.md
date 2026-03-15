# Cyber Ticket NLP Pipeline

Ce projet présente un pipeline simple de traitement du langage naturel (NLP) appliqué à l'analyse de tickets d'incidents en cybersécurité.

L'objectif est de transformer des textes non structurés décrivant des incidents en informations exploitables grâce à des techniques de prétraitement, d'extraction d'entités et de classification.

## Fonctionnalités

- Prétraitement des textes (nettoyage et normalisation)
- Extraction d'entités basée sur des règles (niveau de sévérité, type d'attaque, système concerné, outil)
- Classification de tickets avec un modèle baseline utilisant scikit-learn
- Génération d'un rapport simple d'évaluation

## Structure du projet
```text
cyber-ticket-nlp-pipeline/
│
├── main.py
├── requirements.txt
├── README.md
│
├── data/
│ └── cyber_tickets.csv
│
├── src/
│ ├── preprocessing.py
│ ├── entity_extraction.py
│ └── classification.py
│
└── results/



### Description des composants

- **main.py**  
  Lance l'ensemble du pipeline NLP.

- **src/preprocessing.py**  
  Nettoyage et préparation des données textuelles.

- **src/entity_extraction.py**  
  Extraction d'entités simples à l'aide de règles et d'expressions régulières.

- **src/classification.py**  
  Entraînement et évaluation d'un modèle de classification de tickets.

- **data/cyber_tickets.csv**  
  Dataset synthétique utilisé pour la démonstration.

- **results/**  
  Dossier contenant les résultats générés (métriques et entités extraites).
