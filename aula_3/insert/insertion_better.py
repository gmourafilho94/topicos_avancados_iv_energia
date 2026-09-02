"""
melhorias: 
* verificar se o vetor esta já ordenado
* verificar se ele é menor que 2 
* n - 1 loops por interacao no segundo for?
""" 

sorted = []

def insertion(numbers):
    if (len(numbers) < 2 ): 
        return print(numbers)
    
    while(len(numbers) >= 2):
        for i in range(len(numbers)):
            n_index = min_found(numbers)
            sorted.append(numbers[n_index])
            numbers.pop(n_index) 
                                      
    return print(sorted)
 
def min_found(original_vector):
    min_n = min(original_vector[0:])
    index = original_vector.index(min_n)
    return index
        


n = input()
lista_completa = input()

lista_completa = lista_completa.split()

for v, i in enumerate(lista_completa):
    lista_completa[v] = int(i)
    
insertion(lista_completa)