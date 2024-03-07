#Desafio de criação de um programa que indique quando um aluno esta aprovado ou não com base nos dados de frequencia e em notas de exames.

nota = int(input(" Digite sua nota: "))
frequencia = int(input(" Digite a frequencia: "))


if nota > 100 or nota < 0 or frequencia < 0 or frequencia > 100:
    print(" Nota e/ou frequencia invalida !! ")
else:
    if nota >= 70 and frequencia >= 75:
        print(" Aprovado !!!")
    elif nota >= 40 and nota < 70 and frequencia >= 75:
        print(" Exame !!! ")
    else:
        print(" Reprovado !!! ")
