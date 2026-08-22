\# Data Dictionary



\## Project



\*\*Project:\*\* Public NYISO Power Market Data Analysis  

\*\*Primary objective:\*\* Analyze public NYISO zonal day-ahead prices, real-time prices, load, calendar variables, and historical price patterns.  

\*\*Initial zones:\*\* Zone J and Zone G  

\*\*Initial time frequency:\*\* Hourly  



\## Dataset Inventory



| Dataset | Public Source / URL | Frequency | Geographic Scope | Date Range | Update Cadence | Key Fields | Planned Use | Known Limitations | Automatable? |

|---|---|---|---|---|---|---|---|---|---|

| Day-Ahead Zonal LBMP | NYISO Energy Market \& Operational Data → Pricing Data: https://www.nyiso.com/energy-market-operational-data | Hourly | NYISO load zones; start with G and J | To confirm after download | Daily / historical postings | Timestamp, load zone, LBMP; may include energy, congestion, and loss components | Primary target variable; price-pattern analysis; day-ahead forecast benchmark | Must validate file format, time zone, daylight-saving treatment, units, missing values, and availability history | Yes, subject to public download format and terms |

| Real-Time Zonal LBMP | NYISO Energy Market \& Operational Data → Pricing Data: https://www.nyiso.com/energy-market-operational-data | Sub-hourly or hourly, depending on report | NYISO load zones; start with G and J | To confirm after download | Frequent / daily historical postings | Timestamp, load zone, LBMP; may include energy, congestion, and loss components | Construct hourly real-time price series and DA–RT spread | Must aggregate consistently to hourly level; confirm whether intervals are 5-minute, 15-minute, or hourly; timing alignment is critical | Yes, subject to public download format and terms |

| Day-Ahead vs. Real-Time Spread | Derived from public DA and RT LBMP datasets | Hourly after aggregation | Zone G and Zone J | Same as overlapping DA and RT samples | Updated when underlying data is available | DA LBMP, hourly RT LBMP, DA–RT spread | Secondary target variable; forecast-error and market-difference analysis | Requires careful timestamp, zone, unit, and daylight-saving alignment; a positive spread does not imply a tradable opportunity | Yes, after source datasets are validated |

| Actual Load | NYISO Load Data: https://www.nyiso.com/load-data | To confirm; likely hourly or sub-hourly | NYCA and possibly NYISO zones | To confirm after download | Frequent / daily historical postings | Timestamp, actual load, load zone or NYCA | Demand feature; exploratory relationship between load and price | Confirm whether load includes losses; confirm zonal coverage, units, interval convention, and historical availability | Yes, subject to public download format and terms |

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

