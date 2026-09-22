# Checkpoint — Introduction to Data Structures and Procedural Programming

Solutions des deux problèmes demandés dans le checkpoint GoMyCode, avec les algorithmes en pseudocode, les programmes Python et leurs tests.

## Contenu

| Fichier | Contenu |
| --- | --- |
| [algorithmes.md](algorithmes.md) | Pseudocode : somme des éléments exclusifs, procédure `dot_product`, traitement de n paires et variante avec fonction. |
| [probleme1-algo.py](probleme1-algo.py) | Solution du problème 1 avec des tableaux et des boucles imbriquées. |
| [probleme2-algo.py](probleme2-algo.py) | Procédure avec paramètre de sortie, fonction avec valeur de retour et vérification de n paires de vecteurs. |
| [test_checkpoint.py](test_checkpoint.py) | Tests des résultats attendus et des cas limites. |

## Problème 1 — Somme des éléments exclusifs

On additionne les éléments présents dans **un seul** des deux ensembles.
Les tableaux représentent des ensembles : ils ne contiennent pas de doublons internes.

Pour `A = [3, 1, 7, 9]` et `B = [2, 4, 1, 9, 3]` :

- `7` est présent uniquement dans A.
- `2` et `4` sont présents uniquement dans B.
- `1`, `3` et `9` sont communs et ne sont pas additionnés.
- **Résultat : `7 + 2 + 4 = 13`.**

La somme commence à zéro. Chaque élément de A est recherché dans B, puis chaque élément de B dans A, avec des boucles imbriquées. La solution n'utilise ni `set`, ni dictionnaire.
Pour des tailles m et n, les comparaisons coûtent O(m × n), avec O(1) d'espace auxiliaire.

## Problème 2 — Produit scalaire et orthogonalité

Le produit scalaire est `ps = v1[0] * v2[0] + ... + v1[d-1] * v2[d-1]`.
Deux vecteurs sont orthogonaux lorsque ce produit vaut zéro.

Les deux versions demandées sont fournies :

1. **Procédure `dot_product(v1, v2, ps)`** : les vecteurs sont des paramètres d'entrée ; le résultat est écrit dans le paramètre de sortie `ps`. La procédure ne retourne pas de résultat.
2. **Fonction `dot_product_function(v1, v2)`** : le produit scalaire est retourné puis affecté à une variable par l'appelant.

Python transmet les références des objets par affectation. Il ne permet pas de modifier directement un nombre appartenant à l'appelant. La procédure utilise donc une liste mutable d'un élément (`ps = [0]`) et écrit dans `ps[0]` pour représenter le paramètre de sortie. Les vecteurs d'entrée ne sont pas modifiés.

`check_orthogonality_with_procedure` et `check_orthogonality_with_function` parcourent une liste de **n paires**. Chaque appel calcule le produit en parcourant les coordonnées : la boucle sur les paires contient les appels qui effectuent la boucle sur les coordonnées.
Les vecteurs d'une même paire doivent avoir la même dimension ; une dimension incompatible provoque une erreur explicite.

Les programmes acceptent des coordonnées réelles. Ils considèrent un produit scalaire de valeur absolue inférieure ou égale à `10^-12` comme zéro pour limiter les effets des arrondis flottants. Le pseudocode présente le critère mathématique exact.

Exemples communs aux deux versions :

| v1 | v2 | ps | Résultat |
| --- | --- | --- | --- |
| `[1, 2, 3]` | `[1, 1, -1]` | 0 | Orthogonaux |
| `[1, 2, 3]` | `[-2, 4, -1]` | 3 | Non orthogonaux |
| `[1.5, 2]` | `[2, -1.5]` | 0 | Orthogonaux |
| `[0, 0]` | `[5, 6]` | 0 | Orthogonaux |

Pour n paires de dimension d, le calcul coûte O(n × d). Chaque produit utilise O(1) d'espace auxiliaire ; la liste des résultats utilise O(n).

## Exécution

Python 3 suffit, sans installation de dépendances.

```bash
python3 probleme1-algo.py
python3 probleme2-algo.py
python3 -m unittest -v test_checkpoint.py
```

Pour essayer d'autres vecteurs, modifier la liste `pairs` dans `probleme2-algo.py`. Le nombre de paires est calculé automatiquement avec `len(pairs)`.
