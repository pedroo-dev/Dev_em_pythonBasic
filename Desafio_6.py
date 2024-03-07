LADO1 = float(input(" Insira o primeiro lado: "))
LADO2 = float(input(" Insira o segundo lado: "))
LADO3 = float(input(" Insira o terceiro lado: "))

if LADO1 == LADO2 == LADO3:
    print(" Este é um triangulo equilátero ")
elif LADO1 == LADO2 != LADO3:
    print(" Este é um triangulo isóceles ")
else:
    print(" Este é um triangulo escaleno ")