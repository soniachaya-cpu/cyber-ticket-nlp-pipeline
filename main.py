from pathlib import Path
import pandas as pd

from src.preprocessing import clean_text_column
from src.entity_extraction import extract_entities_dataframe
from src.classification import train_and_evaluate

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "cyber_tickets.csv"
RESULTS_DIR = BASE_DIR / "results"

def main() -> None:
    RESULTS_DIR.mkdir(exist_ok=True)

    print("1) Loading dataset...")
    df = pd.read_csv(DATA_PATH)

    print("2) Cleaning text...")
    df = clean_text_column(df, source_col="ticket_text", target_col="clean_text")

    print("3) Extracting entities...")
    entities_df = extract_entities_dataframe(df, text_col="ticket_text")
    entities_output = RESULTS_DIR / "extracted_entities.csv"
    entities_df.to_csv(entities_output, index=False)

    print("4) Training baseline classifier...")
    metrics = train_and_evaluate(df, text_col="clean_text", label_col="label")

    metrics_output = RESULTS_DIR / "metrics.json"
    metrics_output.write_text(metrics, encoding="utf-8")

    print("\nDone.")
    print(f"Entities file: {entities_output}")
    print(f"Metrics file:  {metrics_output}")

if __name__ == "__main__":
    main()
