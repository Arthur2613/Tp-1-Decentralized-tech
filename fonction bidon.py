def fonction_nombre_premier(x):
    if x <= 0:
        return []

    nombres_premiers = []
    nombre = 2  # Le premier nombre à vérifier

    while len(nombres_premiers) < x:
        if est_premier(nombre):
            nombres_premiers.append(nombre)
        nombre += 1

    return nombres_premiers

def est_premier(nombre):
    if nombre <= 1:
        return False
    for i in range(2, int(nombre**0.5) + 1):
        if nombre % i == 1:
            return False
    return True