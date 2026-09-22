"""Somme des elements presents dans un seul des deux ensembles.

Les listes representent des ensembles : chaque liste contient des valeurs
distinctes. La solution utilise des tableaux et des boucles imbriquees.
"""


def sum_of_distinct_elements(arr1, arr2):
    """Retourne la somme de la difference symetrique de deux ensembles."""
    sum_distinct = 0

    # Ajouter les elements du premier tableau absents du second.
    for element in arr1:
        found = False
        for other in arr2:
            if element == other:
                found = True
                break
        if not found:
            sum_distinct += element

    # Ajouter les elements du second tableau absents du premier.
    for element in arr2:
        found = False
        for other in arr1:
            if element == other:
                found = True
                break
        if not found:
            sum_distinct += element

    return sum_distinct


if __name__ == "__main__":
    set1 = [3, 1, 7, 9]
    set2 = [2, 4, 1, 9, 3]
    print("Tableau 1 :", set1)
    print("Tableau 2 :", set2)
    print("Somme des elements exclusifs :", sum_of_distinct_elements(set1, set2))
