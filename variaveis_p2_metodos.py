#Método  para inscerção de dados em uma lista:  "append" e "insert".

# minha_lista = [1, 2, 3]

# print(" Minha lista ", minha_lista)

# minha_lista.append(64)

# print(" Minha lista ", minha_lista)

# minha_lista.insert(1, 33)
# print(" Minha lista ", minha_lista)

#Método para analisar dados encontrando informações repetidas: "count".

# minha_lista = [1, 2, 3, 4 ,3, 10, 2, 15, 3]
# print(" O numero 3 aparece ", minha_lista.count(3), " vezes ")
# print(" O numero 2 aparece ", minha_lista.count(2), " vezes ")
# print(" O numero 10 aparece ", minha_lista.count(10), " vezes ")

# #Método para remoçao do primeiro dado de uma lista: "remove".
# minha_lista.remove(3)
# print(" Minha lista: ", minha_lista)

# #Método para remoção de dados quando se deseja a remoção de um dado especifico que pode estar repetido e podendo ter a opção de acrescentalo
# #novamente no caso de um erro com o uso do "append".
# elemento = minha_lista.pop(4)
# print(" O elemento retirado da minha lista: ", elemento)
# print(" Minha lista: ", minha_lista)

meu_dicionario = {  
'nome': 'João',   
'idade': 25,   
'cidade':'São Paulo',  
'profissao':'Desenvolvedor',  
'salario': 5000.00,  
'status':'Empregado',  
'linguagens': ['Python','JavaScript','C++'],  
'experiencia': {'anos':3,'empresa':'TechCorp'},  
'projetos': {'ativos':5,'concluidos':12},  
'certificacoes': ['Python Developer','Web Developer'],
}

# Exibindo o dicionário
# print(meu_dicionario)
# print(' Quantidade de projetos concluidos: ', meu_dicionario[' projetos '][' concluidos '])

# print(' A primeira certificação é: ', meu_dicionario['certificacoes'][0])

# print(' Minhas chaves: ', meu_dicionario.keys())
# print(' Os valores são: ', meu_dicionario.values())

# meu_dicionario.clear()
# print(meu_dicionario)

certificacoes = meu_dicionario.pop('certificacoes')
print(certificacoes)
print(meu_dicionario)




