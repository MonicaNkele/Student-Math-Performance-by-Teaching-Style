# Importer les bibliothèques
library(tidyverse)
library(haven)

# Lire le fichier .sav et exporter en DataFrame .csv
df <- read_sav("data/raw/ProjectData.sav")
write_csv(df, "data/raw/NewProjectData.csv")

# Afficher les métadonnées du fichier .sav
attributes(df)

# Afficher les premières lignes
head(df)

# Afficher le nombre de lignes et de colonnes
nrow(df)
ncol(df)

# Afficher les types de données des colonnes
vapply(df, typeof, character(1))
