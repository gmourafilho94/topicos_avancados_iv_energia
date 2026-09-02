
def bubble(numbers):
    
    if len(numbers) < 2: return print(numbers)
    
    sorted = []

    while (len(numbers) >= 2): 
        found = False  
        for j in range(0, len(numbers) - 1): 
                # suspende, compara, retira do numbers, coloca no sorted
                # flag serve para a verificação que achou o vetor completamente ordenado
            if numbers[j] > numbers[j+1]:
                found = True
                aux = numbers[j]    
                numbers[j] = numbers[j+1]   
                numbers[j+1] = aux

        if (found == False):
            for k in range(0, len(numbers)):
                sorted.insert(0, numbers[-1])
                numbers.pop()  
        else: 
            sorted.insert(0, numbers[-1]);
            numbers.pop()
    if numbers:
        sorted.insert(0, numbers.pop());                
    
    return print(sorted)

n = input()
lista_completa = input()

lista_completa = lista_completa.split()

for v, i in enumerate(lista_completa):
    lista_completa[v] = int(i)

    
bubble(lista_completa)
