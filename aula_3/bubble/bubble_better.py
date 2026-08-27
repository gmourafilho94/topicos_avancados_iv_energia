
def bubble(numbers):
    # o que pode ser melhorado nesse algoritmo?
    # a ultima passada nao precisaria ser feita. 
    # como saber se o vetor já está ordenado? [2, 3, 6, 7] -> []
    ordenado = []
    for i in numbers: 
        if (len(ordenado) < len(numbers) -1): return print(numbers)
        for j in range(0, len(numbers)-1): 
            # suspende e compara com o restante ? != bubble_sort;
            if numbers[j] > numbers[j+1]:
                aux = numbers[j]    
                numbers[j] = numbers[j+1]   
                numbers[j+1] = aux
            ordenado.append(numbers[i]);
    return print(numbers)


n = input()
lista_completa = input()

lista_completa = lista_completa.split()

for v, i in enumerate(lista_completa):
    lista_completa[v] = int(i)

    
bubble(lista_completa)
