# Uncorrelated Returns Seeker

# Step 1: Load Libraries & Data
import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt

try:
    import riskfolio as rp
except ImportError:
    print("⚠️ Install 'riskfolio-lib' with: pip install riskfolio-lib")

try:
    import quantstats as qs
except ImportError:
    print("⚠️ Install 'quantstats' with: pip install quantstats")

## Step 1: Define Asset List
assets = [ 
    "BLK", "PFF", "DELL", "LMT", "BA", "RTX", "GD", "NOC", "LHX", "HII",
    "FCT.MI", "ASB.AX", "BOLL", "BAESY", "CACI", "ACN", "RAND",
    "J", "STRL", "GAI", "LDOS", "MCK", "HUM", "HON", "BAH", 
    "SAIC", "GE", "MSFT", "PANW", "NVDA", "AAPL", "GLD", "^GSPC"
]

## Step 2: Collect and format data
print("📥 Downloading price data...")
# download adjuste prices safely 
raw_data = yf.download(assets, start="2016-01-01", end="2025-04-23", group_by="ticker", auto_adjust=False)

# handle multi-index or flat DataFrame depending on structure 
if isinstance(raw_data.columns, pd.MultiIndex):
    data = raw_data.xs("Adj Close", axis=1, level=1)
else:
    # fallback: likely only 1 ticket or different format
    data = raw_data

data = data.dropna(axis=1, how='all')  # Drop assets with no data

## Step 3: Convert Prices to Returns
returns = data.pct_change().dropna()

## Step 4: Calculate Median Returns
median_returns = returns.median().sort_values(ascending=False).to_frame().rename(columns={0: "median_return"})
print("\n📊 Median Returns:\n", median_returns)

# Save to CSV
median_returns.to_csv("median_returns.csv")

## Step 5: Filter High-Performing Assets (median return > 5%)
high_performers = median_returns[median_returns["median_return"] > 0.05]
print("\n⭐ High-Performing Assets (median return > 5%):\n", high_performers)

# Remove assets with zero variance (constant returns)
returns = returns.loc[:, returns.std() > 0]

# Check and remove columns that produce NaNs in correlation matrix
corr = returns.corr()
if corr.isnull().values.any():
    cols_with_nan = corr.columns[corr.isnull().any()]
    print(f"Removing columns with NaN correlation: {list(cols_with_nan)}")
    returns = returns.drop(columns=cols_with_nan)
    
## Step 6: Riskfolio Cluster Plot (if available)
if 'rp' in globals():
    print("\n📈 Plotting cluster dendrogram...")
    rp.plot_clusters(
        returns=returns,
        codependence='pearson',
        linkage='ward',
        k=None,
        max_k=10,
        leaf_order=True,
        dendrogram=True,
        ax=None
    )
    plt.show()

## Step 7: Generate QuantStats Report for a Sample Stock
if 'qs' in globals():
    print("\n📑 Generating QuantStats report for AAPL...")
    qs.reports.html(returns["AAPL"], benchmark=returns["^GSPC"], output="aapl-report.html")
else:
    print("⚠️ Skipping QuantStats report; module not loaded.")



