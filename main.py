# -*- coding: utf-8 -*-

## Import des dépendances

# Librairies
import pandas as pd

# Jeu de données
filename='full_data.csv'
data = pd.read_csv(filename)

#%% Exploration du jeu de données

#%% Informations génériques sur les données

print('\nShape:')
print(data.shape)

print('\nHead:')
print(data.head())

print('\nInfo:')
print(data.info())

print('\nDescribe:')
print(data.describe())

#%% Information spécifiques

print("\nNombre de données manquantes:")
print(data.isna().sum())

print("\nNombre de données en double:")
print(data.duplicated().sum())

#%% Remplacement des données manquantes

# Détermination de la moyenne

# Récupération des données quantitatives
mean = data.mean(numeric_only=True)
print(mean)

# Remplacement des données manquantes par les moyennes
data.fillna(mean, inplace=True)

#%% Suppression des données dupliquées

data.drop_duplicates(inplace=True)
print(data)

#%% Suppression des colonnes vides

data.dropna(how='all', axis=1, inplace=True)
print(data)


#%% Suppression des colonnes avec données redondates

data.drop( [ column for column in data if len(set(data[column])) == 1 ], axis=1, inplace=True )
print(data)

#c bien