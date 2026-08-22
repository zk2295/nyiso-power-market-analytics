\# Data Dictionary



\## Project



\*\*Project:\*\* Public NYISO Power Market Data Analysis  

\*\*Primary objective:\*\* Analyze public NYISO zonal day-ahead prices, real-time prices, load, calendar variables, and historical price patterns.  

\*\*Initial zones:\*\* Zone J and Zone G  

\*\*Initial time frequency:\*\* Hourly  



\## Dataset Inventory



| Dataset | Public Source / URL | Frequency | Geographic Scope | Date Range | Update Cadence | Key Fields | Planned Use | Known Limitations | Automatable? |

|---|---|---|---|---|---|---|---|---|---|

| Day-Ahead Zonal LBMP | NYISO Energy Market & Operational Data → Pricing Data: https://www.nyiso.com/energy-market-operational-data | Hourly | NYISO load zones; initial analysis uses `N.Y.C.` for Zone J; Zone G to be added later | Jan. 1, 2025–Aug. 22, 2026 in initial downloaded sample; Jan. 1–Aug. 21, 2026 overlaps with current load sample | Daily / historical public postings | `Time Stamp`, `Name`, `PTID`, `LBMP ($/MWHr)`, `Marginal Cost Losses ($/MWHr)`, `Marginal Cost Congestion ($/MWHr)` | Primary target variable; Zone J price-pattern analysis; day-ahead forecast benchmark | Timestamp convention and daylight-saving-time treatment require further validation; market data may not capture all physical and operational drivers of prices; Zone G analysis not yet implemented | Yes; successfully compiled multiple public CSV files locally |

| Real-Time Zonal LBMP | NYISO Energy Market \& Operational Data → Pricing Data: https://www.nyiso.com/energy-market-operational-data | Sub-hourly or hourly, depending on report | NYISO load zones; start with G and J | To confirm after download | Frequent / daily historical postings | Timestamp, load zone, LBMP; may include energy, congestion, and loss components | Construct hourly real-time price series and DA–RT spread | Must aggregate consistently to hourly level; confirm whether intervals are 5-minute, 15-minute, or hourly; timing alignment is critical | Yes, subject to public download format and terms |

| Day-Ahead vs. Real-Time Spread | Derived from public DA and RT LBMP datasets | Hourly after aggregation | Zone G and Zone J | Same as overlapping DA and RT samples | Updated when underlying data is available | DA LBMP, hourly RT LBMP, DA–RT spread | Secondary target variable; forecast-error and market-difference analysis | Requires careful timestamp, zone, unit, and daylight-saving alignment; a positive spread does not imply a tradable opportunity | Yes, after source datasets are validated |

| Actual Load | NYISO Load Data: https://www.nyiso.com/load-data | Daily source file containing hourly fields; reshaped to hourly observations for analysis | NYCA system load in initial downloaded sample | Jan. 1, 2026–Aug. 21, 2026; 233 dates overlap with the current Zone J day-ahead LBMP sample | Public historical postings; exact update cadence to be documented | `Year`, `Month`, `Day`, `Hr1`–`Hr24`; `Hr25` appears in source data and is excluded from the initial analysis pending daylight-saving-time treatment | Demand feature; descriptive load-price analysis; later forecasting feature | Source is daily wide-format rather than timestamp-based; `Hr25` requires explicit daylight-saving-time handling; confirm hour-ending versus hour-beginning convention and whether load includes losses before final modeling | Yes; successfully compiled and reshaped public CSV files locally |

| Load Forecast | NYISO Load Data: https://www.nyiso.com/load-data | To confirm | NYCA and possibly NYISO zones | To confirm after download | Published according to NYISO reporting schedule | Forecast timestamp, target operating hour, forecast load, zone or NYCA | Possible forecast-error feature if forecast publication time and actual load are aligned correctly | Must avoid look-ahead bias; confirm when each forecast became publicly available and whether the public historical dataset preserves original forecast vintages | Possibly; only after publication timing is understood |

| Real-Time Fuel Mix | NYISO Real-Time Dashboard: https://www.nyiso.com/real-time-dashboard | Real-time; historical download availability to confirm | NYCA | To confirm | Real-time / dashboard update | Timestamp, fuel category, MW or generation share | Exploratory context; later model feature or narrative explanation | Dashboard display may not provide a clean historical bulk-download dataset; fuel categories may be aggregated | To confirm |

| Generator / Outage Information | NYISO public market and operational postings: https://www.nyiso.com/energy-market-operational-data | To confirm | NYCA / resource-level only where public | To confirm | To confirm | Publicly released system or generator information, if available | Optional later context only; not part of initial model | Do not use nonpublic, generator-specific, market-participant, or employment-derived information; public status must be clear | To confirm |

| Ancillary Services Prices | NYISO Energy Market \& Operational Data → Ancillary Services: https://www.nyiso.com/energy-market-operational-data | To confirm | NYCA and applicable zones | To confirm after download | Daily / historical postings | Timestamp, service type, clearing price, zone where applicable | Future battery-storage and market-conditions analysis | Not required for Project 1; confirm products, units, frequency, and historical format | Yes, subject to public download format and terms |

| Calendar Variables | Self-generated from timestamps | Hourly | N/A | Full project sample | Generated when data is processed | Hour, weekday, weekend flag, month, season, holiday flag | Baseline forecast features | Holiday calendar must be documented; calendar variables do not capture operational conditions | Yes |

| Weather Data | Public weather provider; specific source to be selected later | Hourly | Representative weather stations for NYISO zones | To confirm | Depends on source | Timestamp, temperature, humidity, wind speed, precipitation | Later-phase load and price feature | Station selection, timestamp alignment, missing data, and weather-to-load relationship require careful treatment | Yes, depending on source |



\## Initial Data Priorities



The initial project will use only the following datasets:



1\. Public day-ahead zonal LBMP.

2\. Public actual load data.

3\. Self-generated calendar variables.



The project will add real-time LBMP only after validating hourly aggregation and timestamp alignment. It will add load forecasts, fuel mix, weather, ancillary-service prices, and public outage data only after documenting their availability, timing, and limitations.

## Initial Validation Results

### Day-Ahead LBMP

- Successfully compiled public day-ahead LBMP CSV files into one local dataset.
- Initial combined price-data coverage: Jan. 1, 2025 through Aug. 22, 2026.
- Confirmed that the public location label `N.Y.C.` represents the initial Zone J analysis location.
- The dataset includes hourly timestamps, location names, PTIDs, total LBMP, marginal-loss component, and marginal-congestion component.
- Zone G has not yet been added to the analysis.

### Actual Load

- Successfully compiled public load CSV files into one local dataset.
- Initial load-data coverage: Jan. 1, 2026 through Aug. 21, 2026.
- Source files are in daily wide format with `Year`, `Month`, `Day`, and hourly load fields `Hr1`–`Hr24`.
- The source also contains `Hr25`, which is not included in the initial analysis pending documented daylight-saving-time treatment.
- The initial load dataset was reshaped into hourly observations using timestamps from the daily date fields and the hourly columns.

### Initial Overlap

- The initial Zone J day-ahead LBMP and NYCA actual-load datasets have 233 overlapping calendar dates.
- The overlapping period is Jan. 1, 2026 through Aug. 21, 2026.
- The project will validate duplicate timestamps, missing hours, time conventions, and daylight-saving-time treatment before using the merged data for forecasting or statistical inference.



\## Data Quality Checks Required Before Analysis



For every dataset used in the project, confirm:



\- Data is publicly available from an authorized source.

\- Download URL and date of access are documented.

\- Time zone and daylight-saving-time treatment are understood.

\- Timestamp represents the correct market or operating interval.

\- Units are documented and consistent.

\- Geographic labels and zone names are standardized.

\- Duplicate records are identified.

\- Missing records are identified and treated transparently.

\- Historical coverage is sufficient for chronological train/test splitting.

\- The dataset does not contain nonpublic, employment-derived, or confidential information.

\- Any feature used to forecast a price was publicly available before the forecast target interval.



\## Public-Data Boundary



This repository is an independent personal educational project.



Only publicly available data, personal equipment, personal accounts, and personal time may be used.



No NYISO systems, nonpublic data, internal methodologies, internal model outputs, internal emails, meeting materials, stakeholder discussions, confidential work product, generator-specific information, market-participant information, transmission-system information, or information obtained through employment may be used.



If the public status or timing of any dataset is uncertain, it will not be used.

