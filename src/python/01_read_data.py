import pandas as pd

# Lire les données déjà converties par le script R
df = pd.read_csv('data/processed/data.csv')

# Afficher les métadonnées du fichier
# Les labels texte (ex: Teacher 1=Ruger) ne sont pas dans ce CSV -> voir docs/data_dictionary.md
print(df.info())

# Afficher les premières lignes
print(df.head())

# Afficher le nombre de lignes et de colonnes
print(f"Nombre de lignes: {df.shape[0]}")
print(f"Nombre de colonnes: {df.shape[1]}")

# Afficher les types de données des colonnes
print(df.dtypes)

# Afficher des statistiques descriptives
print(df.describe())
