"""Load the trained brain hemorrhage classifier once for the Django app."""
from pathlib import Path
from tensorflow.keras.models import load_model

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "keras_model.h5"

if not MODEL_PATH.exists():
    raise FileNotFoundError(
        f"Model file not found: {MODEL_PATH}. "
        "Place keras_model.h5 in the project root beside manage.py."
    )

model = load_model(str(MODEL_PATH), compile=False)
