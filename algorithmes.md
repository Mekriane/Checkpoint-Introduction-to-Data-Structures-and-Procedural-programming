# Algorithmes du checkpoint

Les tableaux sont indexés à partir de **0**. `TAILLE(T)` désigne la taille d'un tableau.
`IN` désigne un paramètre d'entrée ; `OUT` désigne un résultat transmis à l'appelant.
`ERREUR` interrompt l'algorithme si une précondition n'est pas respectée.

## Problème 1 — Somme des éléments exclusifs

Chaque tableau représente un ensemble et ne contient donc pas de doublons internes.
Un élément présent dans les deux tableaux ne doit pas être ajouté.

```text
FONCTION SommeElementsDistincts(IN A : TABLEAU DE REELS,
                              IN B : TABLEAU DE REELS) : REEL
VARIABLES
    somme : REEL
    i, j : ENTIER
    trouve : BOOLEEN
DEBUT
    somme <- 0

    POUR i DE 0 A TAILLE(A) - 1 FAIRE
        trouve <- FAUX
        POUR j DE 0 A TAILLE(B) - 1 FAIRE
            SI A[i] = B[j] ALORS
                trouve <- VRAI
            FIN SI
        FIN POUR
        SI NON trouve ALORS
            somme <- somme + A[i]
        FIN SI
    FIN POUR

    POUR i DE 0 A TAILLE(B) - 1 FAIRE
        trouve <- FAUX
        POUR j DE 0 A TAILLE(A) - 1 FAIRE
            SI B[i] = A[j] ALORS
                trouve <- VRAI
            FIN SI
        FIN POUR
        SI NON trouve ALORS
            somme <- somme + B[i]
        FIN SI
    FIN POUR

    RETOURNER somme
FIN

ALGORITHME ExempleSomme
DEBUT
    A <- [3, 1, 7, 9]
    B <- [2, 4, 1, 9, 3]
    ECRIRE SommeElementsDistincts(A, B)  // 7 + 2 + 4 = 13
FIN
```

## Problème 2 — Version avec procédure

Les deux vecteurs d'une paire doivent avoir la même dimension. La dimension peut varier d'une paire à l'autre.
La procédure ne retourne pas de valeur : elle écrit dans `ps`, passé comme paramètre de sortie par référence.

```text
PROCEDURE dot_product(IN v1 : TABLEAU DE REELS,
                      IN v2 : TABLEAU DE REELS,
                      OUT ps : REEL)
VARIABLES
    i : ENTIER
DEBUT
    SI TAILLE(v1) != TAILLE(v2) ALORS
        ERREUR "Dimensions incompatibles"
    FIN SI
    ps <- 0
    POUR i DE 0 A TAILLE(v1) - 1 FAIRE
        ps <- ps + v1[i] * v2[i]
    FIN POUR
FIN

ALGORITHME OrthogonaliteAvecProcedure
VARIABLES
    n, k, d, i : ENTIER
    v1, v2 : TABLEAU DE REELS
    ps : REEL
DEBUT
    LIRE n
    SI n < 0 ALORS
        ERREUR "Le nombre de paires doit etre positif ou nul"
    FIN SI
    POUR k DE 1 A n FAIRE
        LIRE d
        SI d < 0 ALORS
            ERREUR "La dimension doit etre positive ou nulle"
        FIN SI
        CREER v1 ET v2 DE TAILLE d
        POUR i DE 0 A d - 1 FAIRE
            LIRE v1[i], v2[i]
        FIN POUR

        APPELER dot_product(v1, v2, ps)
        SI ps = 0 ALORS
            ECRIRE "Paire", k, ": vecteurs orthogonaux"
        SINON
            ECRIRE "Paire", k, ": vecteurs non orthogonaux"
        FIN SI
    FIN POUR
FIN
```

## Problème 2 — Version avec fonction

Cette variante remplace la procédure précédente. Le résultat est retourné par la fonction, puis affecté à `ps` dans l'algorithme principal.

```text
FONCTION dot_product(IN v1 : TABLEAU DE REELS,
                     IN v2 : TABLEAU DE REELS) : REEL
VARIABLES
    i : ENTIER
    ps : REEL
DEBUT
    SI TAILLE(v1) != TAILLE(v2) ALORS
        ERREUR "Dimensions incompatibles"
    FIN SI
    ps <- 0
    POUR i DE 0 A TAILLE(v1) - 1 FAIRE
        ps <- ps + v1[i] * v2[i]
    FIN POUR
    RETOURNER ps
FIN

ALGORITHME OrthogonaliteAvecFonction
VARIABLES
    n, k, d, i : ENTIER
    v1, v2 : TABLEAU DE REELS
    ps : REEL
DEBUT
    LIRE n
    SI n < 0 ALORS
        ERREUR "Le nombre de paires doit etre positif ou nul"
    FIN SI
    POUR k DE 1 A n FAIRE
        LIRE d
        SI d < 0 ALORS
            ERREUR "La dimension doit etre positive ou nulle"
        FIN SI
        CREER v1 ET v2 DE TAILLE d
        POUR i DE 0 A d - 1 FAIRE
            LIRE v1[i], v2[i]
        FIN POUR

        ps <- dot_product(v1, v2)
        SI ps = 0 ALORS
            ECRIRE "Paire", k, ": vecteurs orthogonaux"
        SINON
            ECRIRE "Paire", k, ": vecteurs non orthogonaux"
        FIN SI
    FIN POUR
FIN
```

En pseudocode, le calcul porte sur des réels mathématiques et teste `ps = 0`.
Dans les versions Python, une tolérance absolue de `10^-12` est utilisée pour le test de zéro afin de tenir compte des arrondis des nombres flottants. C'est un test d'orthogonalité numérique approchée.
