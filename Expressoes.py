# Para numeros inteiros designar a variavel como: INT
# Para números com pontos ou virgulas designar a variavel como: Float

peso = int(input("Digite seu peso"))
altura = float(input("Digite sua altura"))

imc = peso / (altura * altura)

print("Peso ?", peso)
print("altura ?", altura)
print("O seu IMC é: ", imc)
