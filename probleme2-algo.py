def dot_product(v1, v2):
    ps = 0
    n = len(v1)
    for i in range(n):
        ps += v1[i] * v2[i]
    return ps

def check_orthogonality(v1, v2):
    ps = dot_product(v1, v2)
    if ps == 0:
        print("Les vecteurs sont orthogonaux.")
    else:
        print("Les vecteurs ne sont pas orthogonaux.")

v1 = [1, 2, 3]
v2 = [-2, 4, -1]

check_orthogonality(v1, v2)

v3 = [1, 1, 1]
v4 = [-1, -1, -1]

check_orthogonality(v3, v4)
