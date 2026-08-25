import json
import os


def save_json(data: dict, filepath: str) -> None:
    """Sauvegarde un dictionnaire dans un fichier JSON."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def load_json(filepath: str) -> dict:
    """Charge un fichier JSON."""
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)