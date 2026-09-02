
def insertion(numbers):
    for i in range(len(numbers)):
        n_index, n_min = min_found(numbers, i)
        aux = numbers[i] 
        numbers[i] = n_min
        numbers[n_index] = aux 
                                      
    return print(numbers)
 
def min_found(original_vector, position):
    n_min = min(original_vector[position:])
    index = original_vector.index(n_min, position)
    
    return index, n_min
        


n = input()
lista_completa = input()

lista_completa = lista_completa.split()

for v, i in enumerate(lista_completa):
    lista_completa[v] = int(i)
    
insertion(lista_completa)