# -*- coding: utf-8 -*-
"""Death Rate

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VLORcLN2l4iRfqN_xfEQiCAg9gjdK1cH
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd

# Read the dataset into a DataFrame
df = pd.read_csv('/content/drive/Shareddrives/Practera Team Coursework/Air_GHG/Derell- death-rate-from-air-pollution-per-100000.csv')

# Drop rows with missing values
df.dropna(inplace=True)

# Convert data types if needed
# df['column_name'] = df['column_name'].astype('desired_dtype')

# Remove duplicates
df.drop_duplicates(inplace=True)

# Other cleaning operations as needed
# Save the cleaned dataset to a new CSV file
df.to_csv('/content/drive/MyDrive/cleaned_dataset.csv', index=False)

# Display the first few rows of the dataset
print(df.head())

# Get summary statistics of the dataset
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Read the cleaned dataset
cleaned_df = pd.read_csv('/content/drive/MyDrive/cleaned_dataset.csv')

# Display the first few rows
print(cleaned_df.head())

# Check for missing values
print(cleaned_df.isnull().sum())

# Verify other cleaning operations if needed

import pandas as pd

# Read the original dataset into a DataFrame
original_df = pd.read_csv('/content/drive/Shareddrives/Practera Team Coursework/Air_GHG/Derell- death-rate-from-air-pollution-per-100000.csv')
# Make a copy of the original dataset for comparison
uncleaned_df = original_df.copy()

# Read the dataset into a DataFrame
df = pd.read_csv('/content/drive/Shareddrives/Practera Team Coursework/Air_GHG/Derell- death-rate-from-air-pollution-per-100000.csv')

# Check for missing values in the original dataset
missing_values_before = original_df.isnull().sum()

# Drop rows with missing values
df.dropna(inplace=True)

# Calculate how many missing values were removed
missing_values_removed = missing_values_before.sum() - df.isnull().sum().sum()

# Check for duplicates in the original dataset
duplicates_before = original_df.duplicated().sum()

# Remove duplicates
df.drop_duplicates(inplace=True)

# Calculates how many duplicates were removed
duplicates_removed = duplicates_before - df.duplicated().sum()

 # Checks if anything was cleaned
if (missing_values_before != df.isnull().sum()).any():
    print("Missing values were removed. Total missing values removed:", missing_values_removed)

if duplicates_before != df.duplicated().sum():
    print("Duplicate rows were removed.Total duplicates removed:", duplicates_removed)

# Save the cleaned dataset to a new CSV file
df.to_csv('/content/drive/MyDrive/cleaned_dataset.csv', index=False)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the cleaned dataset into a DataFrame
df = pd.read_csv('/content/drive/MyDrive/cleaned_dataset.csv')

# Convert 'Year' column to datetime
df['Year'] = pd.to_datetime(df['Year'], format='%Y')

# Aggregate data by year and calculate average deaths
df_avg = df.groupby('Year')['Deaths that are from all causes attributed to air pollution per 100,000 people, in both sexes aged age-standardized'].mean().reset_index()

# Plot time series
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_avg, x='Year', y='Deaths that are from all causes attributed to air pollution per 100,000 people, in both sexes aged age-standardized', marker='o')
plt.title('Average Deaths attributed to air pollution per 100,000 people over time')
plt.xlabel('Year')
plt.ylabel('Average Deaths per 100,000 people')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

death_rate = df

death_rate.to_csv('death_rate.csv', index=False)