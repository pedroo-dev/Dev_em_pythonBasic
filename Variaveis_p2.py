#Variavel tipo lista
lista_De_frutas = [" maçã ", " banana ", " laranja ", " uva "]

##Variavel tipo tupla
tupla_de_cores = (" vermelho ", " azul ", " verde ", " amarelo ")

#Variavel tipo dicionário
dicionario_de_pessoas = {
    " nome ": " Alice ",
    " idade ": 25,
    " cidade ": " Mauá "
}

# Exibindo os valores das variaveis
print(" Minha lista de frutas: ", lista_De_frutas)
print(" Tupla de cores: ", tupla_de_cores)
print("Dicionário de pessoas:", dicionario_de_pessoas)


# Acessando elementos especificos
#Ex1.
print(" A segunda fruta da minha lista é: ", lista_De_frutas[1])

#Ex2.
print(" A cor verde esta na tupla ", " roxo " in tupla_de_cores)
print(" A cor azul esta na tupla ", " azul " in tupla_de_cores)
print(" O segundo elemento da minha tupla é: ", tupla_de_cores[1])

#Ex3.
print(" A idade de ", dicionario_de_pessoas[" nome "], "é", dicionario_de_pessoas[" idade "],
 " e sua cidade é ", dicionario_de_pessoas[" cidade "])




