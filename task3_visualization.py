import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
df = pd.read_csv("books_data.csv")

fig, axes = plt.subplots(2, 2, figsize=(13, 10))
fig.suptitle("Books.toscrape.com — Data Story", fontsize=16, fontweight="bold")

# 1. Price distribution (histogram)
sns.histplot(df["price_gbp"], bins=20, kde=True, color="steelblue", ax=axes[0, 0])
axes[0, 0].set_title("Price Distribution")
axes[0, 0].set_xlabel("Price (£)")

# 2. Rating counts (bar chart)
rating_counts = df["rating"].value_counts().sort_index()
sns.barplot(x=rating_counts.index, y=rating_counts.values, palette="viridis", ax=axes[0, 1])
axes[0, 1].set_title("Number of Books per Rating")
axes[0, 1].set_xlabel("Rating (stars)")
axes[0, 1].set_ylabel("Count")

# 3. Average price by rating (bar chart) — tests "does rating affect price?"
avg_price_by_rating = df.groupby("rating")["price_gbp"].mean()
sns.barplot(x=avg_price_by_rating.index, y=avg_price_by_rating.values, palette="magma", ax=axes[1, 0])
axes[1, 0].set_title("Average Price by Rating")
axes[1, 0].set_xlabel("Rating (stars)")
axes[1, 0].set_ylabel("Avg Price (£)")

# 4. Stock availability (pie chart)
stock_counts = df["in_stock"].value_counts()
axes[1, 1].pie(
    stock_counts.values,
    labels=["In Stock" if v else "Out of Stock" for v in stock_counts.index],
    autopct="%1.1f%%",
    colors=["mediumseagreen", "salmon"],
    startangle=90,
)
axes[1, 1].set_title("Stock Availability")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("dashboard.png", dpi=150)
print("Saved dashboard.png")
plt.show()
