def remover(lista, valor):
# Verifica se o item a ser removido é o head
    if lista and lista.paciente == valor:
        lista = lista.proximo
    else:
    # Detecta a posição do elemento
        before = None
        navegar = lista
    # Navega pela lista para encontrar o elemento
    while navegar and navegar.paciente != valor:
        before = navegar
        navegar = navegar.proximo
    #print(navegar.data)
    # Remove o item se ele for encontrado
    if navegar:
        before.proximo = navegar.proximo