from pathlib import Path
import pandas as pd


def load_public_nyiso_data(file_path: str | Path) -> pd.DataFrame:
    """
    Load a local CSV downloaded from an authorized public NYISO source.
    No transformations are applied at this stage.
    """
    return pd.read_csv(file_path)


def list_csv_files(directory: str | Path) -> list[Path]:
    """
    Return a sorted list of CSV files within a local directory.
    """
    return sorted(Path(directory).glob("*.csv"))