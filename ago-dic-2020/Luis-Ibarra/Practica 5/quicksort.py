def quickSort(arreglo):
    if len(arreglo) == 0:
        return []

    left = []
    right = []
    pivot = arreglo[0]

    for elemento in arreglo[1:]:
        if elemento < pivot:
            left.append(elemento)
        else:
            right.append(elemento)

    return quickSort(left) + [pivot] + quickSort(right)


n = int(input())
line = input().split()

if n == len(line):
    print(quickSort(line))
else:
    print('Verifica la cantidad de palabras a ordenar')
