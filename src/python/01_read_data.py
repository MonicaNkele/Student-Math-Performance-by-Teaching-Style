# Importer les bibliothèques
import pyreadstat

# Lire le fichier .sav et le convertir en DataFrame pandas
df, meta = pyreadstat.read_sav('data/raw/ProjectData.sav')

# Convertir le DataFrame en fichier CSV
df.to_csv('data/raw/ProjectData.csv', index=False)

# Afficher les métadonnées du fichier .sav
print(meta.column_names_to_labels)

# Afficher les étiquettes de valeurs des variables
print(meta.variable_value_labels)

# Afficher les premières lignes
print(df.head())

# Afficher le nombre de lignes et de colonnes
print(meta.number_rows)

print(meta.number_columns)

# Afficher les types de données des colonnes
print(df.dtypes)
