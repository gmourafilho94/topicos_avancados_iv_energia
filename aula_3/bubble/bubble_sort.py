def bubble(numbers):
    for i in numbers:
        for j in range(0, len(numbers)-1): 
            if numbers[j] > numbers[j+1]:
                aux = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = aux
                                  
    return print(numbers)


n = input()
lista_completa = input()

lista_completa = lista_completa.split()

for v, i in enumerate(lista_completa):
    lista_completa[v] = int(i)

    
bubble(lista_completa)
