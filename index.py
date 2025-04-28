import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Fix font issue globally
plt.rcParams['font.family'] = 'DejaVu Sans'

plt.style.use("seaborn-v0_8-whitegrid")
sns.set_palette("Set2")

file_path = "Electric_Vehicle_Population_Data (1).csv"
df = pd.read_csv(file_path)

df.dropna(subset=['Electric Vehicle Type', 'Make', 'Model', 'County', 'City', 'Model Year'], inplace=True)

print("=== HEAD ===")
print(df.head(), "\n")

print("=== TAIL ===")
print(df.tail(), "\n")

print("=== INFO ===")
print(df.info(), "\n")

print("=== DESCRIBE ===")
print(df.describe(include='all'), "\n")

print("=== SHAPE ===")
print("Rows:", df.shape[0], "Columns:", df.shape[1], "\n")

print("=== MISSING VALUES ===")
print(df.isnull().sum(), "\n")

# Pie Chart for EV Types
type_counts = df['Electric Vehicle Type'].value_counts()
plt.figure(figsize=(6, 6))
type_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['#66c2a5', '#fc8d62'])
plt.title('Proportion of EV Types (BEV vs PHEV)')
plt.ylabel('')
plt.tight_layout()
plt.show()

# Bar chart for EV Types over Model Year
type_year = df.groupby(['Model Year', 'Electric Vehicle Type']).size().unstack().fillna(0)
type_year.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='Set3')
plt.title("Trend of EV Types Over Model Years")
plt.xlabel("Model Year")
plt.ylabel("Number of Vehicles")
plt.tight_layout()
plt.show()

# Top 10 Electric Vehicle Manufacturers
top_makes = df['Make'].value_counts().head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_makes.index, y=top_makes.values)
plt.title('Top 10 Electric Vehicle Manufacturers')
plt.xlabel('Make')
plt.ylabel('Registrations')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Top 10 EV Models
df['Make_Model'] = df['Make'] + " " + df['Model']
top_models = df['Make_Model'].value_counts().head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_models.index, y=top_models.values)
plt.title('Top 10 EV Models')
plt.xlabel('Make and Model')
plt.ylabel('Registrations')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Top 10 Counties by EV Registration
top_counties = df['County'].value_counts().head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_counties.index, y=top_counties.values)
plt.title('Top 10 Counties by EV Registration')
plt.xlabel('County')
plt.ylabel('Registrations')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Top 10 Cities by EV Registration
top_cities = df['City'].value_counts().head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_cities.index, y=top_cities.values)
plt.title('Top 10 Cities by EV Registration')
plt.xlabel('City')
plt.ylabel('Registrations')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# EV Registrations Over Model Years (Line Plot)
yearly = df['Model Year'].value_counts().sort_index()
plt.figure(figsize=(10, 5))
sns.lineplot(x=yearly.index, y=yearly.values, marker='o', linewidth=2.5)
plt.title('EV Registrations Over Model Years')
plt.xlabel('Model Year')
plt.ylabel('Number of EVs')
plt.tight_layout()
plt.show()

# Distribution of BEVs and PHEVs Per Year (Countplot)
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Model Year', hue='Electric Vehicle Type', palette='Set2')
plt.title('Distribution of BEVs and PHEVs Per Year')
plt.xlabel('Model Year')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Estimated Annual CO2 Savings
avg_annual_miles = 11500
co2_per_mile_ice = 0.411
df['Estimated_CO2_Saved_kg'] = avg_annual_miles * co2_per_mile_ice
total_co2_saved = df['Estimated_CO2_Saved_kg'].sum() / 1e6

plt.figure(figsize=(7, 5))
sns.barplot(x=["Estimated Annual CO2 Reduction (Million kg)"], y=[total_co2_saved], color="#8da0cb")
plt.title('Estimated Annual CO2 Savings by EVs')
plt.ylabel('Million kg CO2 Saved')
plt.tight_layout()
plt.show()

# Correlation Heatmap
numerical_df = df.select_dtypes(include=['float64', 'int64'])
plt.figure(figsize=(8, 5))
sns.heatmap(numerical_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Between Numerical Features')
plt.tight_layout()
plt.show()
