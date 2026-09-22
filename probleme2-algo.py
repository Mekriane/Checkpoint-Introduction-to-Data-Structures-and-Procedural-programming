"""Produit scalaire et orthogonalite de n paires de vecteurs reels."""

from math import isclose


ZERO_TOLERANCE = 1e-12


def dot_product(v1, v2, ps):
    """Procedure : ecrit le produit scalaire dans le parametre de sortie ps.

    ps est une liste d'un element, par exemple [0]. Modifier ps[0] permet
    a l'appelant de recuperer le resultat sans valeur de retour.
    Les vecteurs v1 et v2 sont des parametres d'entree et restent inchanges.
    """
    if len(v1) != len(v2):
        raise ValueError("Les deux vecteurs doivent avoir la meme dimension.")
    if len(ps) != 1:
        raise ValueError("ps doit etre une liste contenant un seul element.")

    ps[0] = 0
    for i in range(len(v1)):
        ps[0] += v1[i] * v2[i]


def dot_product_function(v1, v2):
    """Fonction : retourne le produit scalaire des deux vecteurs."""
    if len(v1) != len(v2):
        raise ValueError("Les deux vecteurs doivent avoir la meme dimension.")

    ps = 0
    for i in range(len(v1)):
        ps += v1[i] * v2[i]
    return ps


def check_orthogonality_with_procedure(vector_pairs):
    """Traite n paires avec la procedure ; retourne (produit, orthogonal)."""
    results = []
    ps = [0]
    n = len(vector_pairs)

    # Boucle externe sur les paires, boucle interne dans dot_product.
    for pair_index in range(n):
        v1, v2 = vector_pairs[pair_index]
        dot_product(v1, v2, ps)
        orthogonal = isclose(ps[0], 0.0, rel_tol=0.0, abs_tol=ZERO_TOLERANCE)
        results.append((ps[0], orthogonal))

    return results


def check_orthogonality_with_function(vector_pairs):
    """Meme traitement de n paires, avec une fonction qui retourne ps."""
    results = []
    n = len(vector_pairs)

    for pair_index in range(n):
        v1, v2 = vector_pairs[pair_index]
        ps = dot_product_function(v1, v2)
        orthogonal = isclose(ps, 0.0, rel_tol=0.0, abs_tol=ZERO_TOLERANCE)
        results.append((ps, orthogonal))

    return results


def print_results(title, results):
    print(title)
    for pair_number, (ps, orthogonal) in enumerate(results, start=1):
        status = "orthogonaux" if orthogonal else "non orthogonaux"
        print(f"Paire {pair_number} : ps = {ps:g} -> {status}")


if __name__ == "__main__":
    pairs = [
        ([1, 2, 3], [1, 1, -1]),
        ([1, 2, 3], [-2, 4, -1]),
        ([1.5, 2], [2, -1.5]),
        ([0, 0], [5, 6]),
    ]
    print(f"Verification de {len(pairs)} paires de vecteurs")
    print_results("Version avec procedure :", check_orthogonality_with_procedure(pairs))
    print_results("Version avec fonction :", check_orthogonality_with_function(pairs))
