import math

def dot(a, b):
    sum=0
    n=len(a)
    n=len(b)
    for i in range(n):
        sum+=(a[i]*b[i])
    return sum

def norm(a):
    suma=0
    n=len(a)
    for i in range(n):
        suma+=a[i]*a[i]
    return math.sqrt(suma)

def cosine_similarity(a, b):
    print((dot(a,b))/(norm(a)*norm(b)))

cosine_similarity([1, 2, 3], [1, 2, 3])    # what do you expect?
cosine_similarity([1, 0], [0, 1])          # what do you expect?
cosine_similarity([1, 2, 3], [2, 4, 6])    # what do you expect?