\# Project Charter



\## Project Title



Public NYISO Power Market Data Analysis: Zonal Price and Day-Ahead / Real-Time Spread Study



\## Project Objective



Develop a reproducible, public-data analysis of the relationship between NYISO wholesale electricity prices, electricity demand, calendar conditions, and historical price behavior.



The initial analysis will examine whether publicly available variables can explain or forecast hourly zonal day-ahead Locational-Based Marginal Prices (LBMPs) and the difference between day-ahead and real-time prices.



The project is intended to demonstrate disciplined power-market data analysis, forecasting methodology, and clear communication of limitations. It is not intended to create or recommend a live trading strategy.



\## Business Question



What publicly available variables are associated with hourly NYISO zonal day-ahead prices and day-ahead versus real-time price spreads?



More specifically:



\- How do price patterns vary by hour, weekday, month, and season?

\- How closely are zonal prices associated with system or zonal load?

\- Do historical price lags improve simple benchmark forecasts?

\- When do day-ahead and real-time prices diverge most significantly?

\- Are relationships different between Zone J and Zone G?



\## Market and Geographic Scope



\- Market: New York Independent System Operator (NYISO)

\- Initial zones: Zone J and Zone G

\- Potential future expansion: Additional NYISO zones if results demonstrate a clear analytical purpose

\- Market products:

&#x20; - Day-ahead zonal LBMP

&#x20; - Real-time zonal LBMP

&#x20; - Day-ahead versus real-time price spread

\- Time frequency: Hourly

\- Initial sample period: To be determined based on the availability and quality of public data



\## Target Variables



The project will evaluate one or more of the following target variables:



1\. Hourly day-ahead zonal LBMP.

2\. Hourly real-time zonal LBMP, aggregated consistently to hourly frequency if necessary.

3\. Hourly day-ahead versus real-time price spread:



&#x20;  DA–RT Spread = Day-Ahead LBMP − Real-Time LBMP



The first phase will prioritize day-ahead LBMP as the primary target variable. The day-ahead versus real-time spread will be added after the data-alignment process has been validated.



\## Candidate Features



The initial feature set may include:



\- Hour of day.

\- Day of week.

\- Weekend indicator.

\- Month.

\- Season.

\- Federal holiday indicator.

\- Historical day-ahead price lags.

\- Historical real-time price lags, if applicable.

\- Public actual load data.

\- Public load-forecast data, if available and aligned appropriately.

\- Load forecast error, calculated only where both public forecast and actual load are available.

\- Public temperature or weather proxy data in a later project phase.



All features will be documented in the data dictionary, including source, timing, frequency, limitations, and treatment of missing values.



\## Analytical Approach



\### Phase 1: Data validation and exploratory analysis



\- Download and organize only publicly available data.

\- Standardize timestamps, zones, price units, and time frequency.

\- Identify missing values, duplicates, outliers, daylight-saving-time issues, and incomplete intervals.

\- Visualize hourly, daily, weekly, and seasonal price patterns.

\- Compare Zone J and Zone G price behavior.

\- Examine the relationship between public load and prices.



\### Phase 2: Benchmark forecasting model



Develop a transparent historical-average benchmark using combinations of:



\- Hour of day.

\- Weekday versus weekend.

\- Month or season.

\- Holiday indicator.



The benchmark model will establish a performance floor that more advanced models must exceed.



\### Phase 3: Transparent predictive models



Test interpretable models such as:



\- Linear regression.

\- Regularized linear regression, if needed.

\- Random forest regression.

\- Gradient-boosting or XGBoost regression, only if the data and benchmark justify additional complexity.



The project will prioritize reproducibility, reasonable economic interpretation, and robust validation over model complexity.



\## Evaluation Framework



Models will be evaluated using a clear chronological train, validation, and out-of-sample test split.



Primary evaluation metrics:



\- Mean Absolute Error (MAE).

\- Root Mean Squared Error (RMSE).

\- Mean Absolute Percentage Error (MAPE), only where appropriate for price levels.

\- Directional accuracy for price changes or day-ahead versus real-time spreads.

\- Error distribution by hour, season, and price regime.



The project will compare every model against the historical-average benchmark and clearly report periods in which the model performs poorly.



\## Expected Deliverables



\- Reproducible Python data-ingestion and cleaning workflow.

\- Data dictionary describing all public data sources and fields.

\- Exploratory data analysis notebook.

\- Baseline forecasting notebook.

\- Model-comparison notebook.

\- Charts and tables saved in the outputs folder.

\- GitHub README describing methodology, findings, limitations, and how to reproduce the project.

\- A concise two-page market-analysis memo summarizing the final results.



\## Limitations



Publicly available data cannot capture all drivers of NYISO market outcomes. Limitations may include:



\- Incomplete visibility into generator-specific conditions.

\- Limited detail on transmission constraints and operational decisions.

\- Timing differences between public data publications and market outcomes.

\- Weather, fuel, outage, import, and dispatch factors not fully captured by the initial model.

\- Market outcomes affected by system conditions that may not be represented in public datasets.

\- Correlation does not establish causation.

\- Historical backtesting does not demonstrate that a model would be profitable or suitable for trading.



\## Data and Confidentiality Boundary



This is an independent personal educational project.



All analysis will use only publicly available data, personal equipment, personal accounts, and personal time.



The project will not use, copy, upload, summarize, reproduce, or rely on NYISO systems, files, software, code, nonpublic data, internal methodologies, internal model outputs, internal emails, meeting materials, stakeholder discussions, generator-specific information, market-participant information, transmission-system information, or confidential work product.



If the public status of any information is uncertain, it will not be used.



\## Definition of Success



The project will be successful if it produces a clean, reproducible public-data workflow and a well-documented analysis that:



\- Identifies economically plausible patterns in NYISO zonal prices.

\- Establishes an honest historical-average benchmark.

\- Evaluates whether additional public variables improve forecast accuracy.

\- Clearly communicates uncertainty and limitations.

\- Demonstrates market-analysis, Python, data-quality, and technical-communication skills.

