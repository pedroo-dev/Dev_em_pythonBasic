# 7a. Realizar uma contagem regressiva com while: de 10 a 1.


# contador = 10

# while contador < 11 and contador > 0:
#     print( contador )
#     contador = contador -1


# 7b. Realizar a soma de uma faixa de números com comando WHILE:

# num_inicial = int(input("Digite o num inicial para soma: "))
# num_final = int(input("Digite o num final para soma: "))

# num = num_inicial
# soma = 0

# while num <= num_final:
#     soma = soma + num
#     num += 1
# print(" Resultado da soma: ", soma)


# 7c. Realizar a soma de uma faixa de números com comando FOR:

# num_inicial = int(input("Digite o num inicial para soma: "))
# num_final = int(input("Digite o num final para soma: "))

# num = num_inicial
# soma = 0

# for num in range(num_inicial, num_final+1):
#     soma = soma + num
# print(" A soma dos numeros é: ", soma)


# 7d. Faça um programa utilizando while e listas, que permita o usuario
# escrever o nome de cinco pessoas e os mostre na tela.

# nomes = []

# for i in range(5):
#     nome = input(" Digite o nome: ")
#     nomes.append(nome)
# print(" Minha lista de nomes é:", nomes)

# 7e. Soma de uma faixa de numero: Peça ao usuário para inserir um número
# inicial e mostre o intervalo de números

# Solução 1 invertendo a contagem com o FOR
# num_inicial = int(input(" Digite um numero inicial: "))
# num_final = int(input(" Digite o numero final: "))


# if num_inicial < num_final:
#     for num in range(num_final, num_inicial+1):
#         print(num)
# else:
#     for num in range(num_final, num_inicial+1):
#         print(num)


# # Solução 2 Com uma lógica executavel apenas com o pyton.
# if num_inicial > num_final:
#     num_final, num_final = num_final, num_inicial

# for num in range(num_inicial, num_final+1):
#     print(num)


# Faça um programa que leia 5 numeros e informe o maior número

numeros = []

for i in range(5):
    num = int(input(" Digite o numero: "))
    numeros.append(num)
    print(numeros)

maior = 0

for num in numeros:
    if maior < num:
        maior = num

print(" O maior numero é: ", maior)
