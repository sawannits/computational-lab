import pandas as pd
import numpy as np

df = pd.read_csv('titanic.csv')

print("--- Original Data Info ---")
print(df.info())

df['Age'] = df['Age'].fillna(df['Age'].median())
df['Cabin'] = df['Cabin'].fillna('Unknown')

if df['Embarked'].isnull().sum() > 0:
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

df['Sex'] = df['Sex'].str.strip().str.lower()
df['Name'] = df['Name'].str.strip('"')

df.drop_duplicates(inplace=True)

df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

print("\n--- Cleaned Data Info ---")
print(df.info())

print("\n--- First 5 Cleaned Rows ---")
print(df.head())

df.to_csv('cleaned_titanic.csv', index=False)
