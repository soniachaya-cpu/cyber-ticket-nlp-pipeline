import json
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

def train_and_evaluate(df: pd.DataFrame, text_col: str, label_col: str) -> str:
    X_train, X_test, y_train, y_test = train_test_split(
        df[text_col],
        df[label_col],
        test_size=0.3,
        random_state=42,
        stratify=df[label_col],
    )

    model = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=1)),
        ("clf", LogisticRegression(max_iter=1000)),
    ])

    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    report = classification_report(y_test, preds, output_dict=True)
    accuracy = accuracy_score(y_test, preds)

    output = {
        "accuracy": round(float(accuracy), 4),
        "classes": sorted(df[label_col].unique().tolist()),
        "report": report,
    }
    return json.dumps(output, indent=2)
