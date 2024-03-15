# -*- coding: utf-8 -*-
"""gen_promising_subset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PkyEUfzU60nE5GtGqfA-mvsogpDX2UsN
"""



from scipy.spatial import KDTree
import numpy as np
from itertools import combinations
from collections import Counter

def nearNeighborsSet(data, k, input_x, n=0, y=None):
    """
    Identifie les k+n voisins les plus proches de input_x dans data en utilisant un KDTree.
    """
    # Séparation des vecteurs de caractéristiques et des étiquettes
    features = [point[0] for point in data]
    labels = [point[1] for point in data]

    # Construction de KDTree avec seulement les vecteurs de caractéristiques
    tree = KDTree(features)
    dists, indices = tree.query([input_x], k=k+n)

    # Récupération des voisins en utilisant les indices retournés par KDTree
    neighbors = [(features[i], labels[i]) for i in indices[0]]

    if y is not None and n > 0:
        neighbors_without_y = [neighbor for neighbor in neighbors if neighbor[1] != y]
        if len(neighbors_without_y) < k:
            neighbors_with_y = [neighbor for neighbor in neighbors if neighbor[1] == y][:k - len(neighbors_without_y)]
            neighbors = neighbors_without_y + neighbors_with_y
        else:
            neighbors = neighbors_without_y[:k]
    else:
        neighbors = neighbors[:k+n]

    return neighbors

def mostFreqLabel(data, k, input_x, y=None, n=0):
    """
    Trouve l'étiquette la plus fréquente parmi les k+n voisins les plus proches.
    """
    neighbors = nearNeighborsSet(data, k, input_x, n=n, y=y)
    labels = [neighbor[1] for neighbor in neighbors]
    most_common_label = Counter(labels).most_common(1)[0][0]
    return most_common_label

def generateSubsetsR1(data, k, input_x, n, min_rmv):
    """
    Génère des sous-ensembles R1 à partir des k+n éléments les plus proches de x.
    """
    nearest_neighbors = nearNeighborsSet(data, k, input_x, n=n)
    subsets_r1 = [list(subset) for r in range(min_rmv, len(nearest_neighbors) + 1)
                                  for subset in combinations(nearest_neighbors, r)]
    return subsets_r1

def generateSubsetsR2(data, k, input_x, n, len_r1):
    """
    Supprime d'abord tous les k+n éléments les plus proches de x dans data, puis crée tous les sous-ensembles
    d'au plus n-len(r1) éléments avec le nouvel ensemble de données.
    """
    nearest_neighbors = nearNeighborsSet(data, k, input_x, n=n)

    # Utiliser la conversion en tuple pour la comparaison et éviter l'erreur
    reduced_data =  [x for x in data if not any(np.array_equal(x, element) for element in nearest_neighbors)]

    max_subset_size = n - len_r1
    subsets_r2 = []
    for r in range(1, max_subset_size + 1):
        for subset in combinations(reduced_data, r):
            subsets_r2.append(subset)
    return subsets_r2


def GenPromisingSubset(data, input_x, n, y):
    """
    Utilise une recherche binaire pour trouver min_rmv, puis génère des sous-ensembles R1 et R2.
    """
    promising_subsets = []
    Kset = [2, 4, 6]  # Ensemble des valeurs de K à considérer

    for k in Kset:

        # Initialiser les variables pour la recherche binaire
        start, end = 1, n  # On commence à 1 car 0 ne changerait pas l'ensemble des voisins

        # Recherche binaire pour trouver le min_rmv optimal
        while start <= end:
            mid = (start + end) // 2
            if y == mostFreqLabel(data, k, input_x, y, mid):
                start = mid + 1
            else:
                end = mid - 1

        min_rmv = start  # Le nombre minimal de suppressions pour changer la prédiction

        # Générer des sous-ensembles R1 avec au moins min_rmv éléments
        subsets_r1 = generateSubsetsR1(data, k, input_x, n, min_rmv)

        for r1 in subsets_r1:
            # Générer des sous-ensembles R2 avec le reste des données, jusqu'à n-len(r1) éléments
            subsets_r2 = generateSubsetsR2(data, k, input_x, n, len(r1))

            for r2 in subsets_r2:
                # Combinaison de R1 et R2 pour former un sous-ensemble prometteur
                R = r1 + list(r2)
                # Retirer les éléments de R de l'ensemble de données original pour obtenir le sous-ensemble final
                T_without_R = [x for x in data if not any(np.array_equal(x, element) for element in R)]

                promising_subsets.append(T_without_R)

    return promising_subsets


from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)

# Créer une liste de paires (x, y) à partir de X et y

xy = list(zip(X, y))
# print((xy))

# Afficher les 5 premières paires
print(len(GenPromisingSubset(data=xy[:149], input_x=[4.9, 3. , 1.4, 0.2], n=3, y='0')))