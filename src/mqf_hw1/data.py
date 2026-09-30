from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[2] / "data"

def load_data() -> pd.DataFrame:
    """Load the project dataset."""
    return pd.read_excel(DATA_DIR / "asset_class_return_assignment_1.xlsx")