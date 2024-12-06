#!/usr/bin/env python3

# O código pede as notas da disciplina para soma-las e realizar a média do total, mas ele possui algumas falhas.

# PROBLEMAS:
# A entrada de dados não possui processo de validação, permitindo números maiores do que dez e menores do que zero
# Não é pedido para adicionar contabilizar a nota no contador_notas, então se torna um loop infinito pois ele nunca sai de zero
# A média da disciplina é definida ao se dividir o total por 10, quando a condição é do número de notas ser 11, a divisão poderia ser igual ao contador para evitar essa diferença

# Definindo total como zero:
total = 0

# Definindo CONTcontador_notas como zero:
contador_notas = 0

# Loop para pedir 10 notas:
while contador_notas < 10:
    entrada = input(f"Digite a nota {contador_notas + 1}: ")  # Entrada da nota

    # Validação da entrada:
    try:
        nota = float(entrada)  # Define a entrada como nota e converte seu valor para float
        if 0 <= nota <= 10:  # Verifica se o valor da nota está entre 0 e 10
            total += nota  # Soma o valor da nota ao total
            contador_notas += 1  # Contabiliza a nota ao contador de notas
        else:
            print("Nota inválida. Insira uma nota entre 0 e 10.") # Acusa se a entrada é um número fora do intervalo de 0 a 10
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.") # Acusa se a entrada não for um número

# Calcula a média da disciplina
media = total / contador_notas # Calcula a média ao dividir o total pelo valor no contador de notas

# Imprime a média da disciplina
print(f"A média da disciplina é: {media:.2f}") # Mostra o resultado final
