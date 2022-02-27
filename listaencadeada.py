# lista ordenada  - annessa

lista = list()
for a in range(1, 4):
    contador = int(input(f'Digite um numero: '))
    if a == 1 or contador >= lista[-1]:
        lista.append(contador)
    elif contador <= lista[0]:
        lista.insert(0, contador)
    elif lista[0] <= contador <= lista[1]:
        lista.insert(1, contador)
    elif lista[1] <= contador <= lista[2]:
        lista.insert(2, contador)
    elif lista[2] <= contador <= lista[3]:
        lista.insert(3, contador)
    print(lista)