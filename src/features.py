import pandas as pd


def create_calendar_features(
    df: pd.DataFrame,
    timestamp_col: str,
) -> pd.DataFrame:
    """
    Add transparent calendar features for exploratory analysis and baseline models.
    """
    featured = df.copy()

    timestamps = pd.to_datetime(
        featured[timestamp_col],
        errors="coerce",
    )

    featured["hour"] = timestamps.dt.hour
    featured["day_of_week"] = timestamps.dt.dayofweek
    featured["is_weekend"] = featured["day_of_week"].isin([5, 6]).astype(int)
    featured["month"] = timestamps.dt.month
    featured["year"] = timestamps.dt.year

    featured["season"] = (
        (timestamps.dt.month % 12 + 3) // 3
    ).map(
        {
            1: "Winter",
            2: "Spring",
            3: "Summer",
            4: "Fall",
        }
    )

    return featured