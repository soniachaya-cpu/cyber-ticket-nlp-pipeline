import re
import pandas as pd

def normalize_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s\-_]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def clean_text_column(df: pd.DataFrame, source_col: str, target_col: str) -> pd.DataFrame:
    out = df.copy()
    out[target_col] = out[source_col].astype(str).apply(normalize_text)
    return out
