def encontrar_maximo(lista):
    if not lista: 
        return None
    maximo = lista[0]  
    for num in lista:  
        if num > maximo:  
            maximo = num
    return maximo

numeros = [3, 5, 7, 2, 8, 1, 4]
print(encontrar_maximo(numeros))  
