\# Data Dictionary



| Dataset | Source | Frequency | Geographic Scope | Key Fields | Planned Use | Public URL | Notes |

|---|---|---|---|---|---|---|---|

| Day-ahead LBMP | NYISO public market data | Hourly | NYISO zones | Timestamp, zone, LBMP | Target variable | To be added | Validate time zone and missing values |

| Real-time LBMP | NYISO public market data | Hourly or sub-hourly | NYISO zones | Timestamp, zone, LBMP | DA–RT spread | To be added | Aggregate consistently with DA data |

| Actual load | NYISO public load data | Hourly or sub-hourly | NYISO / zones | Timestamp, load | Demand feature | To be added | Check load definition |

| Load forecast | NYISO public load data | Hourly | NYISO / zones | Timestamp, forecast load | Forecast-error feature | To be added | Confirm availability and timing |

| Calendar variables | Self-generated | Hourly | N/A | Hour, day, month, holiday | Model features | N/A | Generated in Python |

