# Dictionnaire des données — ProjectData.sav

## Source
Fichier Kaggle (https://www.kaggle.com/datasets/soumyadiptadas/students-math-score-for-different-teaching-style/data)
Cas d'école sur les performances en mathématiques de 217 élèves de 4e avec 3 enseignantes et 2 méthodes pédagogiques

## Vue d'ensemble
- Observations : 217 (1 valeur manquante sur Teacher, ligne 217)
- Variables : 7
- Unité d'observation : un élève par ligne

## Variables
| Nom | Type | Valeur | Remarques |
|---|---|---|---|
| Student | identifiant | 1-217 | Identifiant unique de l'élève |
| Teacher | catégorielle nominale | 1=Ruger, 2=Smith, 3=Wesson | 1 valeur manquante (ligne 217) |
| Gender | catégorielle binaire | 1=Female, 2=Male |  |
| Ethnic | catégorielle nominale | 1=Asian, 2=African-American, 3=Hispanic, 4=Caucasian | Origine ethnique des élèves |
| Freeredu | catégorielle binaire | 1=Free lunch, 2=Paid lunch | Eligibilité au repas gratuit (facteur socio-économique) |
| Score | continue | numerique | Scores au test standardisé de maths|
| wesson | catégorielle binaire | 0=Ruger_Smith, 1=Wesson | Regroupement des méthodes (standard vs traditionnelle) pour comparer les 2 méthodes |

## Pipeline de données
Lancer le fichier ("src/r/01_read_data.R") en premier.

La conversion du .sav en .csv est effectué en R grâce à ("src/r/01_read_data.R") qui lit le ".sav" original et produit "data/processed/data.csv" avec les codes numériques bruts (labels texte disponibles ci-dessus, pas dans le fichier).
Ce choix évite la duplication de logique de conversion entre les deux langages ; les labels restent consultables dans le tableau ci-dessus.
Le script Python ("src/python/01_read_data.py") lit ensuite ce même fichier.

## Limites connues
- Pas de variable de niveau/habileté (high-ability/low-ability) dans le dataset, malgré la proposition de Ms. Wesson à ce sujet dans le cas d'école — non testable empiriquement avec ces données.
- 1 valeur manquante sur Teacher (ligne 217).
