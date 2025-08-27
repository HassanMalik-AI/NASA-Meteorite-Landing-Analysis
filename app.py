# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: for clean plots
sns.set(style="whitegrid")

# Step 1: Load dataset
url = "G:\SEABORN\Meteorite_Landings (2).csv"
df = pd.read_csv(url)

# Step 2: Basic cleaning
df = df.dropna(subset=['reclat', 'reclong', 'mass (g)', 'year'])

# Convert 'year' to datetime, then extract just the year
df['year'] = pd.to_datetime(df['year'], errors='coerce')
df = df.dropna(subset=['year'])
df['year'] = df['year'].dt.year

# Step 3: EDA Visualizations

# 3.1 Total meteorites per year
plt.figure(figsize=(14, 6))
yearly_counts = df.groupby('year').size()
sns.lineplot(x=yearly_counts.index, y=yearly_counts.values, color='blue')
plt.title("Total Meteorites Found Per Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.grid(True)
plt.tight_layout()
plt.show()

# 3.2 Top 10 meteorite classes
plt.figure(figsize=(10, 6))
top_classes = df['recclass'].value_counts().head(10)
sns.barplot(x=top_classes.values, y=top_classes.index, palette="viridis")
plt.title("Top 10 Meteorite Classes")
plt.xlabel("Count")
plt.ylabel("Class")
plt.tight_layout()
plt.show()

# 3.3 Mass distribution (log scale)
plt.figure(figsize=(10, 6))
sns.histplot(df['mass (g)'], bins=100, kde=True, log_scale=(True, True), color='orange')
plt.title("Mass Distribution of Meteorites")
plt.xlabel("Mass (g) - Log Scale")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 3.4 Boxplot for outlier detection (log scale)
plt.figure(figsize=(10, 2))
sns.boxplot(x=df['mass (g)'], color='green')
plt.xscale("log")
plt.title("Boxplot of Meteorite Mass (Log Scale)")
plt.tight_layout()
plt.show()

# 3.5 Meteorite landings by coordinates
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='reclong', y='reclat', size='mass (g)', alpha=0.5, sizes=(10, 200))
plt.title("Meteorite Landing Locations Around the World")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.tight_layout()
plt.show()
