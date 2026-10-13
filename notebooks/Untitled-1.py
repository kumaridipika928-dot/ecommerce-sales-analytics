# %%
print("Hello, E-Commerce Analytics!")

# %%
import pandas as pd

# %%
import pandas as pd

data = {
    "Order_ID": [1001, 1002, 1003],
    "Product": ["Laptop", "Mouse", "Keyboard"],
    "Sales": [50000, 1000, 2500]
}

df = pd.DataFrame(data)

df


# %%
df.shape


# %%
df.columns

# %%
import pandas as pd

df = pd.read_excel("../data/raw/sample_-_superstore.xls")

df.head()

# %%
import xlrd

print("xlrd is working!")


# %%
import pandas as pd

file_path = "sample_-_superstore.xls"

df = pd.read_excel(r"data/raw/sample_-_superstore.xls")

print(df.head())
print(df.shape)
print(df.columns)

# %%
import os

print("Python is currently looking in:")
print(os.getcwd())

print("\nFiles/folders here:")
print(os.listdir())

# %%
print(os.listdir("data"))


# %%
# ============================================
# E-COMMERCE DATASET LOADING
# ============================================

import pandas as pd
import os
import glob

# 1. Show where Python is currently working
print("Current folder:")
print(os.getcwd())

# 2. Search for Excel files inside the project
excel_files = glob.glob("data/raw/*.xls") + glob.glob("data/raw/*.xlsx")

print("\nExcel files found:")

if len(excel_files) == 0:
    print("NO EXCEL FILE FOUND!")
    print("\nLet's check what is inside the data folder:")
    
    if os.path.exists("data"):
        print(os.listdir("data"))
        
        if os.path.exists("data/raw"):
            print("\nFiles inside data/raw:")
            print(os.listdir("data/raw"))
    else:
        print("The 'data' folder itself was not found.")

else:
    for file in excel_files:
        print(file)

    # 3. Automatically select the first Excel file
    file_path = excel_files[0]

    print("\nUsing this file:")
    print(file_path)

    # 4. Read the Excel file
    df = pd.read_excel(file_path)

    # 5. Show basic information
    print("\nDataset loaded successfully! ✅")

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nDataset shape:")
    print(df.shape)

    print("\nColumn names:")
    print(df.columns.tolist())

    print("\nDataset information:")
    print(df.info())

# %%
import os

print("CURRENT LOCATION:")
print(os.getcwd())

print("\nWHAT IS HERE:")
for item in os.listdir():
    print(item)

# %%
import pandas as pd
import os
import glob

# Current location
print("Current folder:")
print(os.getcwd())

# Go one folder UP from notebooks
project_folder = ".."

# Look inside data/raw
excel_files = (
    glob.glob("../data/raw/*.xls") +
    glob.glob("../data/raw/*.xlsx")
)

print("\nExcel files found:")

if len(excel_files) == 0:
    print("❌ NO EXCEL FILE FOUND")
    
    print("\nFiles in data/raw:")
    
    if os.path.exists("../data/raw"):
        print(os.listdir("../data/raw"))
    else:
        print("❌ data/raw folder does not exist")

else:
    for file in excel_files:
        print("✅", file)

    # Select the Excel file
    file_path = excel_files[0]

    print("\nLoading:")
    print(file_path)

    # Read Excel
    df = pd.read_excel(file_path)

    print("\n✅ DATASET LOADED SUCCESSFULLY!")

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

# %%
# ============================================
# STEP 2 - UNDERSTAND THE DATASET
# ============================================

# Number of rows and columns
print("Dataset Shape:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns.tolist())

# First 5 rows
print("\nFirst 5 Rows:")
display(df.head())

# Data types and missing values
print("\nDataset Information:")
df.info()

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# %%
# ============================================
# STEP 3 - BASIC STATISTICS
# ============================================

print("Basic Statistics:")
display(df.describe())

# %%
# ============================================
# STEP 4 - CHECK DUPLICATES
# ============================================

print("Number of duplicate rows:")
print(df.duplicated().sum())

# %%
# ============================================
# STEP 5 - DATA CLEANING
# ============================================

# Make a copy of the original dataset
cleaned_df = df.copy()

print("Original shape:", cleaned_df.shape)

# --------------------------------------------
# 1. Remove duplicate rows
# --------------------------------------------

duplicates = cleaned_df.duplicated().sum()

print("Duplicate rows:", duplicates)

cleaned_df = cleaned_df.drop_duplicates()

print("Shape after removing duplicates:", cleaned_df.shape)


# --------------------------------------------
# 2. Check missing values
# --------------------------------------------

print("\nMissing values:")
print(cleaned_df.isnull().sum())


# --------------------------------------------
# 3. Check column data types
# --------------------------------------------

print("\nData types:")
print(cleaned_df.dtypes)

# %%
# ============================================
# STEP 6 - CHECK IMPORTANT COLUMNS
# ============================================

print("Columns in our dataset:")

for i, column in enumerate(cleaned_df.columns, 1):
    print(i, "->", column)

# %%
# ============================================
# STEP 7 - CONVERT DATE COLUMNS
# ============================================

if "Order Date" in cleaned_df.columns:
    cleaned_df["Order Date"] = pd.to_datetime(
        cleaned_df["Order Date"],
        errors="coerce"
    )

if "Ship Date" in cleaned_df.columns:
    cleaned_df["Ship Date"] = pd.to_datetime(
        cleaned_df["Ship Date"],
        errors="coerce"
    )

print("Date columns converted successfully!")

print(cleaned_df[["Order Date", "Ship Date"]].head())

# %%
# ============================================
# STEP 8 - CHECK NUMERIC COLUMNS
# ============================================

numeric_columns = cleaned_df.select_dtypes(
    include="number"
).columns

print("Numeric columns:")
print(numeric_columns.tolist())

print("\nSummary:")
display(cleaned_df[numeric_columns].describe())

# %%
# ============================================
# STEP 9 - KEY BUSINESS KPIs
# ============================================

# Total Sales
total_sales = cleaned_df["Sales"].sum()

# Total Profit
total_profit = cleaned_df["Profit"].sum()

# Total Orders
total_orders = cleaned_df["Order ID"].nunique()

# Total Customers
total_customers = cleaned_df["Customer ID"].nunique()

# Profit Margin
profit_margin = (total_profit / total_sales) * 100


print("========== E-COMMERCE KPIs ==========")

print(f"Total Sales      : ${total_sales:,.2f}")
print(f"Total Profit     : ${total_profit:,.2f}")
print(f"Total Orders     : {total_orders:,}")
print(f"Total Customers  : {total_customers:,}")
print(f"Profit Margin    : {profit_margin:.2f}%")

# %%
# ============================================
# STEP 10 - PRODUCT & CATEGORY ANALYSIS
# ============================================

# Sales by Category
category_sales = (
    cleaned_df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("Sales by Category:")
display(category_sales)


# Profit by Category
category_profit = (
    cleaned_df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("Profit by Category:")
display(category_profit)


# Top 10 Products by Sales
top_products = (
    cleaned_df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("Top 10 Products by Sales:")
display(top_products)

# %%
# ============================================
# STEP 11 - REGIONAL ANALYSIS
# ============================================

region_sales = (
    cleaned_df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("Sales by Region:")
display(region_sales)


region_profit = (
    cleaned_df.groupby("Region")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("Profit by Region:")
display(region_profit)

# %%
# ============================================
# STEP 12 - MONTHLY SALES TREND
# ============================================

cleaned_df["Month"] = cleaned_df["Order Date"].dt.to_period("M")

monthly_sales = (
    cleaned_df.groupby("Month")["Sales"]
    .sum()
)

print("Monthly Sales:")
display(monthly_sales)

# %%
# ============================================
# STEP 13 - SALES TREND VISUALIZATION
# ============================================

import matplotlib.pyplot as plt

monthly_sales.plot(
    kind="line",
    figsize=(12, 6),
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# %%
# ============================================
# STEP 14 - CUSTOMER ANALYSIS
# ============================================

# Sales generated by each customer
customer_sales = (
    cleaned_df.groupby("Customer ID")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("Top 10 Customers by Sales:")
display(customer_sales.head(10))


# Profit generated by each customer
customer_profit = (
    cleaned_df.groupby("Customer ID")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 Customers by Profit:")
display(customer_profit.head(10))

# %%
# ============================================
# STEP 15 - RFM ANALYSIS
# ============================================

# Make sure Order Date is a date
cleaned_df["Order Date"] = pd.to_datetime(
    cleaned_df["Order Date"],
    errors="coerce"
)

# Choose a reference date
reference_date = cleaned_df["Order Date"].max() + pd.Timedelta(days=1)

rfm = cleaned_df.groupby("Customer ID").agg({
    "Order Date": lambda x: (reference_date - x.max()).days,
    "Order ID": "nunique",
    "Sales": "sum"
})

# Rename columns
rfm.columns = ["Recency", "Frequency", "Monetary"]

print("RFM Analysis:")
display(rfm.head())

# %%
# ============================================
# STEP 16 - RFM SCORES
# ============================================

rfm["R_Score"] = pd.qcut(
    rfm["Recency"],
    4,
    labels=[4, 3, 2, 1],
    duplicates="drop"
)

rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    4,
    labels=[1, 2, 3, 4]
)

rfm["M_Score"] = pd.qcut(
    rfm["Monetary"],
    4,
    labels=[1, 2, 3, 4],
    duplicates="drop"
)

# Convert scores to numbers
rfm["R_Score"] = rfm["R_Score"].astype(int)
rfm["F_Score"] = rfm["F_Score"].astype(int)
rfm["M_Score"] = rfm["M_Score"].astype(int)

# Overall RFM score
rfm["RFM_Score"] = (
    rfm["R_Score"].astype(str)
    + rfm["F_Score"].astype(str)
    + rfm["M_Score"].astype(str)
)

print("RFM scores created!")
display(rfm.head(10))

# %%


# ============================================
# STEP 17 - CUSTOMER SEGMENTS
# ============================================

def segment_customer(row):

    if row["R_Score"] >= 3 and row["F_Score"] >= 3 and row["M_Score"] >= 3:
        return "VIP Customers"

    elif row["R_Score"] >= 3 and row["F_Score"] >= 2:
        return "Loyal Customers"

    elif row["R_Score"] >= 3:
        return "Recent Customers"

    elif row["R_Score"] <= 2 and row["F_Score"] >= 3:
        return "At Risk Customers"

    else:
        return "Low Engagement"


rfm["Segment"] = rfm.apply(segment_customer, axis=1)

print("Customer Segments:")
display(rfm["Segment"].value_counts())

# %%
# ============================================
# STEP 18 - CUSTOMER SEGMENT CHART
# ============================================

segment_counts = rfm["Segment"].value_counts()

segment_counts.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Customer Segments")
plt.xlabel("Customer Segment")
plt.ylabel("Number of Customers")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# %%
# ============================================
# STEP 19 - PROFITABILITY ANALYSIS
# ============================================

# Profit by product
product_profit = (
    cleaned_df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values()
)

print("10 Most Loss-Making Products:")
display(product_profit.head(10))

print("\n10 Most Profitable Products:")
display(product_profit.tail(10).sort_values(ascending=False))

# %%
# ============================================
# STEP 20 - CATEGORY PROFITABILITY
# ============================================

category_analysis = (
    cleaned_df.groupby("Category")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .sort_values("Profit")
)

# Calculate profit margin
category_analysis["Profit Margin %"] = (
    category_analysis["Profit"]
    / category_analysis["Sales"]
    * 100
)

display(category_analysis)

# %%
# ============================================
# STEP 21 - SUB-CATEGORY ANALYSIS
# ============================================

subcategory_analysis = (
    cleaned_df.groupby("Sub-Category")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .sort_values("Profit")
)

subcategory_analysis["Profit Margin %"] = (
    subcategory_analysis["Profit"]
    / subcategory_analysis["Sales"]
    * 100
)

print("Sub-Category Performance:")
display(subcategory_analysis)

# %%
# ============================================
# STEP 22 - HIGH SALES BUT LOW/NEGATIVE PROFIT
# ============================================

product_analysis = (
    cleaned_df.groupby("Product Name")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

# Products with negative profit
loss_products = (
    product_analysis[
        product_analysis["Profit"] < 0
    ]
    .sort_values("Sales", ascending=False)
)

print("High-Sales Loss-Making Products:")
display(loss_products.head(15))

# %%
# ============================================
# STEP 23 - SUB-CATEGORY PROFIT CHART
# ============================================

subcategory_analysis["Profit"].sort_values().plot(
    kind="bar",
    figsize=(12, 6)
)

plt.title("Profit by Sub-Category")
plt.xlabel("Sub-Category")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %%
cleaned_df["Discount"].value_counts().sort_index()


# %%
discount_profit = cleaned_df.groupby("Discount")["Profit"].agg(
    ["sum", "mean"]
).reset_index()

discount_profit.columns = ["Discount", "Total Profit", "Average Profit"]

discount_profit

# %%
def discount_group(discount):
    if discount == 0:
        return "No Discount"
    elif discount <= 0.10:
        return "Low (1-10%)"
    elif discount <= 0.30:
        return "Medium (11-30%)"
    else:
        return "High (31%+)"

cleaned_df["Discount Group"] = cleaned_df["Discount"].apply(discount_group)

cleaned_df[["Discount", "Discount Group"]].head()

# %%
discount_analysis = cleaned_df.groupby("Discount Group").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Average_Profit=("Profit", "mean")
).reset_index()

discount_analysis

# %%
discount_analysis["Profit Margin %"] = (
    discount_analysis["Profit"] /
    discount_analysis["Sales"] * 100
)

discount_analysis

# %%
plt.figure(figsize=(8,5))

plt.bar(
    discount_analysis["Discount Group"],
    discount_analysis["Profit"]
)

plt.title("Profit by Discount Group")
plt.xlabel("Discount Group")
plt.ylabel("Total Profit")

plt.xticks(rotation=20)
plt.show()

# %%
high_discount = cleaned_df[
    cleaned_df["Discount"] >= 0.30
].sort_values("Profit")

high_discount[[
    "Order ID",
    "Product Name",
    "Sales",
    "Discount",
    "Profit"
]].head(10)

# %%
plt.figure(figsize=(8,5))

plt.scatter(
    cleaned_df["Discount"],
    cleaned_df["Profit"],
    alpha=0.5
)

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")

plt.show()

# %%
print(df.columns)

# %%
print(locals().keys())

# %%
correlation = cleaned_df["Discount"].corr(cleaned_df["Profit"])

print("Correlation between Discount and Profit:", correlation)



