from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('WorldCupMatches.csv')
df_goals = pd.read_csv("goals.csv")

print(df.head())

df['Total Goals'] = df["Home Team Goals"] + df["Away Team Goals"]

print(df.head())

# Styling
sns.set_style("whitegrid")
sns.set_context("poster", font_scale=0.8)

f, ax = plt.subplots(figsize=(12,7))

ax = sns.barplot(x=df["Year"], y=df["Total Goals"], data=df)

ax.set_title("Average Goals Scored in Each Year")

plt.show()

#print(df_goals.head())

sns.set_context("notebook", font_scale=1.25)

f, ax2 = plt.subplots(figsize=(12,7))

ax2 = sns.barplot(x=df_goals["year"], y=df_goals["goals"], data=df_goals, palette="Spectral")

ax2.set_title("Distribution of Goals Scored in Each Year")

plt.show()
