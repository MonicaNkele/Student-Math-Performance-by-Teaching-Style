# Performance des élèves en mathématiques selon la méthode pédagogique

## Contexte
Ce projet est un cas d'école simulé.
L'objectif est de vérifier si les différences de performance en mathématiques des élèves de 4e sont dues aux méthodes pédagogiques utilisées par les enseignantes (standard-based VS traditional).
Au niveau personnel, ce projet permet de s'exercer sur Python et R pour consolider des compétences pour un avenir professionnel dans la recherche.

## Source des données
Fichier Kaggle (https://www.kaggle.com/datasets/soumyadiptadas/students-math-score-for-different-teaching-style/data)

## Structure du dépôt
```
student-math-performance-by-teaching-style/
├── README.md
├── data/
│   ├── raw/                # fichier .sav original, jamais modifié
│   └── processed/          # versions nettoyées (.csv ou .parquet)
├── notebooks/              # exploration (Jupyter et/ou R Markdown)
├── src/                    # fonctions réutilisables (python/ et r/)
├── outputs/
│   ├── figures/
│   └── tables/
├── docs/                   # protocole d'analyse, dictionnaire des variables
├── requirements.txt        # dépendances python
├── packages.R              # dépendances R
└── .gitignore
```

## Installation / Prérequis
- Python : `pip install -r requirements.txt`
- R : `Rscript packages.R`

## Comment reproduire l'analyse
1. Lancer `src/r/01_read_data.R` (génère `data/processed/data.csv`)
2. Lancer `src/python/01_read_data.py` (lit ce même fichier)

## Résultats
<!-- à compléter après l'étape d'analyse -->

## Limites
- Pas de variable de niveau/habileté (high-ability/low-ability) dans le dataset, malgré la proposition de Ms. Wesson à ce sujet dans le cas d'école — non testable empiriquement avec ces données.
- 1 valeur manquante sur Teacher (ligne 217).


## Compétences démontrées
- Nettoyage de données
- Gestion de valeurs manquantes
- Bilinguisme Python/R
- Documentation et structuration de projet reproductible
- Réflexion critique sur un dataset

## Auteure
- https://github.com/MonicaNkele
- https://www.linkedin.com/in/monica-danielle-nkele/
