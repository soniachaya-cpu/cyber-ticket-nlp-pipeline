import re
import pandas as pd

SEVERITY_PATTERNS = {
    "critical": r"\bcritical\b",
    "high": r"\bhigh\b",
    "medium": r"\bmedium\b",
    "low": r"\blow\b",
}

ATTACK_PATTERNS = {
    "phishing": r"\bphishing\b",
    "malware": r"\bmalware\b",
    "ransomware": r"\bransomware\b",
    "credential_access": r"\bcredential(s)?\b|\blogin\b|\bpassword\b",
    "suspicious_activity": r"\bsuspicious\b|\bunknown\b|\bunusual\b",
}

SYSTEM_PATTERNS = {
    "vpn": r"\bvpn\b",
    "email": r"\bemail\b|\boutlook\b",
    "server": r"\bserver\b",
    "workstation": r"\blaptop\b|\bworkstation\b|\bdesktop\b",
    "firewall": r"\bfirewall\b",
    "database": r"\bdatabase\b|\bdb\b",
}

TOOL_PATTERNS = {
    "microsoft_365": r"\bmicrosoft 365\b|\bm365\b",
    "jira": r"\bjira\b",
    "okta": r"\bokta\b",
    "crowdstrike": r"\bcrowdstrike\b",
    "aws": r"\baws\b",
    "azure": r"\bazure\b",
}

def _first_match(text: str, patterns: dict) -> str:
    for label, pattern in patterns.items():
        if re.search(pattern, text, flags=re.IGNORECASE):
            return label
    return "unknown"

def extract_entities(text: str) -> dict:
    return {
        "severity": _first_match(text, SEVERITY_PATTERNS),
        "attack_type": _first_match(text, ATTACK_PATTERNS),
        "system": _first_match(text, SYSTEM_PATTERNS),
        "tool": _first_match(text, TOOL_PATTERNS),
    }

def extract_entities_dataframe(df: pd.DataFrame, text_col: str) -> pd.DataFrame:
    rows = []
    for _, row in df.iterrows():
        entities = extract_entities(str(row[text_col]))
        rows.append({
            "ticket_id": row["ticket_id"],
            "ticket_text": row[text_col],
            **entities
        })
    return pd.DataFrame(rows)
