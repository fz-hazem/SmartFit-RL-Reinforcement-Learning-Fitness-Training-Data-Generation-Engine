import os
import pytest
from src.data_gen.generator import generate_dataset
from src.utils.io import load_json


def test_generate_dataset(tmp_path):
    # Dossier temporaire géré par pytest
    output_dir = tmp_path / "data"

    generate_dataset(num_users=2, days=5, output_dir=str(output_dir))

    # Vérification de l'existence des fichiers
    user_1_file = output_dir / "user_1_data.json"
    assert os.path.exists(user_1_file)

    # Validation de la structure du JSON
    data = load_json(str(user_1_file))
    assert "profile" in data
    assert "history" in data
    assert len(data["history"]) == 5
    assert data["profile"]["user_id"] == 1