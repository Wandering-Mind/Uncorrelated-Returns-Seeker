# Uncorrelated-Returns-Seeker


## References
# https://www.washingtontechnology.com/rankings/top-100/2025/
# https://en.wikipedia.org/wiki/Top_100_Contractors_of_the_U.S._federal_government

This Python script helps identify high-performing assets with potentially uncorrelated returns by analyzing historical price data, calculating median returns, and visualizing asset clusters. It leverages yfinance for data collection, pandas for data manipulation, matplotlib and seaborn for visualization, and optionally riskfolio-lib for advanced portfolio optimization and quantstats for performance reporting.

## Features
Asset Data Download: Automatically downloads historical adjusted close prices for a predefined list of assets using yfinance.

Return Calculation: Converts price data into daily percentage returns.

Median Return Analysis: Calculates and displays the median return for each asset, sorted in descending order.

High-Performing Asset Identification: Filters and highlights assets with a median return greater than a specified threshold (default: 5%).

Correlation Handling: Cleans data by removing assets with zero variance or columns that would produce NaN values in the correlation matrix.

Cluster Plotting (Optional): If riskfolio-lib is installed, it generates a cluster dendrogram to visualize the codependence (correlation) between assets, aiding in the identification of uncorrelated groups.

Performance Reporting (Optional): If quantstats is installed, it generates a comprehensive HTML performance report for a sample asset (default: AAPL) against a benchmark (default: ^GSPC).

Prerequisites
Before running the script, ensure you have the following Python libraries installed. You can install them using pip:

pip install pandas yfinance seaborn matplotlib
pip install riskfolio-lib # Optional, for cluster plotting
pip install quantstats    # Optional, for performance reporting

## Getting Started
1. Clone the Repository (or save the script)
If this script is part of a larger repository, clone it:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Otherwise, save the provided Python code as uncorrelated_returns_seeker.py.

2. Run the Script
Execute the script from your terminal:

python uncorrelated_returns_seeker.py

Configuration
You can easily modify the following parameters directly within the script:

assets: The list of ticker symbols for the assets you want to analyze.

assets = [
    "BLK", "PFF", "DELL", "LMT", "BA", "RTX", "GD", "NOC", "LHX", "HII",
    "FCT.MI", "ASB.AX", "BOLL", "BAESY", "CACI", "ACN", "RAND",
    "J", "STRL", "GAI", "LDOS", "MCK", "HUM", "HON", "BAH",
    "SAIC", "GE", "MSFT", "PANW", "NVDA", "AAPL", "GLD", "^GSPC"
]

start and end dates: The date range for downloading historical price data.

raw_data = yf.download(assets, start="2016-01-01", end="2025-04-23", group_by="ticker", auto_adjust=False)

High-Performing Asset Threshold: The 0.05 value (5%) in high_performers can be adjusted.

high_performers = median_returns[median_returns["median_return"] > 0.05]

QuantStats Sample Asset and Benchmark:

qs.reports.html(returns["AAPL"], benchmark=returns["^GSPC"], output="aapl-report.html")

Output
When the script runs, it will:

Print messages indicating data download progress.

Display a table of median returns for all assets.

Display a table of high-performing assets (median return > 5%).

If riskfolio-lib is installed, a plot window will appear showing the cluster dendrogram.

If quantstats is installed, it will generate an aapl-report.html file in the same directory, containing a detailed performance analysis for AAPL.

Contributing
Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please open an issue or submit a pull request.

License
This project is open-sourced under the MIT License. See the LICENSE file for more details.
