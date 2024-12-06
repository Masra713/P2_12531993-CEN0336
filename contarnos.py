#!/usr/bin/env python3

# Árvore do exercício:

arvore = {
        "Filo1": {
            "Classe1": {
                "Ordem1": {
                    "Familia1": {},
                    "Familia2": {}
                },
                "Ordem2": {
                    "Familia3": {
                        "Genero3": {},
                        "Genero4": {}
                    }
                }
            },
            "Classe2": {
                "Ordem3": {},
                "Ordem4": {
                    "Familia4": {},
                    "Familia5": {
                        "Genero1": {},
                        "Genero2": {
                            "Especie1": {},
                            "Especie2": {}
                        }
                    }
                }
            }
        }
}

# Função para contagem:
def contar_nos(arvore):
    if not arvore:
        total = 1 # Adiciona 1 no total caso o dicionário esteja vazio, para contar as "folhas"
    else:
        total = 1 # Adiciona 1 no total caso o dicionário tenha elementos, caso seja um "galho"
    for no in arvore:
        total += contar_nos(arvore[no]) # Gera a recursividade da função em toda a "árvore"
    return total # Retorna o valor total
    
print(contar_nos(arvore)-1) # Mostra o resultado, o "-1" é para retirar o valor da própria "árvore" que atua como "semente" (no caso, eu não estou considerando como um nó)
