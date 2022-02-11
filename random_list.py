from random import randint

# Retorna uma lista com 10 números aleatórios entre 0 e 100
def random_list():
    lista = []
    
    for i in range(0, 10):
        lista.append(randint(0, 100))
    return lista

if (__name__ =="__main__"):
   random_list()
