def merge_piles(piles):
    lista_organizada = []

    while True:
        # Declara um menor valor inicial e seu índice
        menor = piles[0][len(piles[0]) - 1]
        index = 0

        # Atravessa todas as pilhas
        for pos, i in enumerate(piles):
            # SE o menor for maior que o topo da pilha atual
            # ele e seu índice são substituídos
            if menor > i[len(i) - 1]:
                menor = i[len(i) - 1]
                index = pos
        
        # Adiciona o valor na lista final e deleta ela das pilhas
        lista_organizada.append(menor)
        piles[index].pop(len(piles[index]) - 1)
        
        # SE a pilha atual estiver vazia remove ela das pilhas
        if len(piles[index]) == 0:
            piles.pop(index)
        
        # SE todas a pilhas estiverem vazias interrompe a repetição
        if len(piles) == 0:
            break
    
    return lista_organizada
        

def patience_sort(arr):
    piles = []

    # Atravessa o array
    for i in arr:
        
        # SE ainda não exite nenhuma pilha
        if len(piles) == 0:

            # Cria uma pilha e adiciona o primeiro elemento
            pilha = []
            pilha.append(i)
            piles.append(pilha)
        
        # SE NÃO checa as pilhas já existentes
        else:
            # Condição pra uma nova pilha
            new_pile = True
            
            # Atravessa todas as pilhas
            for j in piles:
                # Adiciona o elemento SE ele for menor do que
                # o topo da pilha atual
                if i < j[len(j) - 1]:
                    j.append(i)
                    new_pile = False
                    break
            
            # SE uma nova pilha for necessária
            if new_pile:
                
                # Cria uma nova pilha e adiciona o elemento dentro dela
                pilha = []
                pilha.append(i)
                piles.append(pilha)

    print(f"Pilhas: {piles}")
    lista_organizada = merge_piles(piles)
    return(lista_organizada)

arr = [6, 12, 2, 8, 3, 7]
if (__name__ =="__main__"):
   patience_sort(arr)