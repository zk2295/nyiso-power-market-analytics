import pandas as pd


def clean_price_data(
    df: pd.DataFrame,
    timestamp_col: str,
    zone_col: str,
    price_col: str,
) -> pd.DataFrame:
    """
    Standardize a public price dataset after source fields are identified.
    """
    cleaned = df.copy()

    cleaned[timestamp_col] = pd.to_datetime(
        cleaned[timestamp_col],
        errors="coerce",
    )

    cleaned = cleaned.dropna(
        subset=[timestamp_col, zone_col, price_col]
    )

    cleaned = cleaned.drop_duplicates()

    return cleaned.sort_values(
        [timestamp_col, zone_col]
    ).reset_index(drop=True)


def clean_load_data(
    df: pd.DataFrame,
    timestamp_col: str,
    load_col: str,
) -> pd.DataFrame:
    """
    Standardize a public hourly load dataset after it has been reshaped.
    """
    cleaned = df.copy()

    cleaned[timestamp_col] = pd.to_datetime(
        cleaned[timestamp_col],
        errors="coerce",
    )

    cleaned = cleaned.dropna(
        subset=[timestamp_col, load_col]
    )

    cleaned = cleaned.drop_duplicates()

    return cleaned.sort_values(
        timestamp_col
    ).reset_index(drop=True)


def validate_hourly_time_index(
    df: pd.DataFrame,
    timestamp_col: str,
) -> pd.DataFrame:
    """
    Summarize time gaps to identify missing or irregular intervals.
    """
    timestamps = (
        pd.to_datetime(df[timestamp_col], errors="coerce")
        .dropna()
        .sort_values()
    )

    return (
        timestamps.diff()
        .value_counts()
        .sort_index()
        .rename_axis("time_difference")
        .reset_index(name="count")
    )