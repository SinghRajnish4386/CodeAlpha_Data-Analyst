import pandas as pd

df = pd.read_csv("books_data.csv")

print("=" * 60)
print("1. DATA STRUCTURE")
print("=" * 60)
print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
print("\nData types:")
print(df.dtypes)
print("\nFirst 5 rows:")
print(df.head())

print("\n" + "=" * 60)
print("2. MISSING VALUES / DATA ISSUES")
print("=" * 60)
print(df.isnull().sum())
print(f"\nDuplicate rows: {df.duplicated().sum()}")

print("\n" + "=" * 60)
print("3. SUMMARY STATISTICS")
print("=" * 60)
print(df.describe())

print("\n" + "=" * 60)
print("4. MEANINGFUL QUESTIONS TO EXPLORE")
print("=" * 60)

# Q1: What's the price distribution?
print(f"\nAverage price: £{df['price_gbp'].mean():.2f}")
print(f"Min price: £{df['price_gbp'].min():.2f}")
print(f"Max price: £{df['price_gbp'].max():.2f}")

# Q2: Does rating correlate with price? (hypothesis test)
correlation = df["price_gbp"].corr(df["rating"])
print(f"\nCorrelation between price and rating: {correlation:.3f}")
if abs(correlation) < 0.1:
    print("-> Very weak/no relationship between price and rating.")
else:
    print("-> Some relationship exists between price and rating.")

# Q3: How many books are in stock vs out of stock?
print("\nStock availability:")
print(df["in_stock"].value_counts())

# Q4: Rating distribution
print("\nRating distribution:")
print(df["rating"].value_counts().sort_index())

# Q5: Anomaly check — any unusually priced books? (outliers via IQR)
Q1 = df["price_gbp"].quantile(0.25)
Q3 = df["price_gbp"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df["price_gbp"] < lower_bound) | (df["price_gbp"] > upper_bound)]
print(f"\nPrice outliers found (IQR method): {len(outliers)}")
if len(outliers) > 0:
    print(outliers[["title", "price_gbp"]].head())

print("\nEDA complete. Findings ready to feed into Task 3 (Visualization).")
