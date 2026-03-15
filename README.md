<<<<<<< HEAD
# Cyber Ticket NLP Pipeline

A small NLP project to classify synthetic cybersecurity incident tickets and extract simple entities from text.

## Features
- Text preprocessing
- Rule-based entity extraction (severity, attack type, system, tool)
- Baseline ticket classification with scikit-learn
- Simple evaluation report

## Project structure
- `main.py`: run the full pipeline
- `src/preprocessing.py`: clean and prepare text
- `src/entity_extraction.py`: extract entities with regex rules
- `src/classification.py`: train and evaluate classifier
- `data/cyber_tickets.csv`: synthetic dataset
- `results/`: generated outputs

## Quick start
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```
=======
# cyber-ticket-nlp-pipeline
>>>>>>> 2fb9d889a5e8e0be49643a80798b8167ca4f4474
