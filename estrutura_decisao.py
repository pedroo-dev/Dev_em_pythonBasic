# if

idade = int(input(" Digite sua idade: "))

# if idade < 18:
#     print(" Você deve aguardar até as 12h para ir embora !!")
# else:
#     if idade >= 18 and idade < 30:
#         print(" Seu horário é as 11h45 ")
#     else:
#         print(" Você esta livre ")


if idade < 18:
    print(" Você deve aguardar até as 12h para ir embora !!")
elif idade >= 18 and idade < 30:
    print(" Seu horário é as 11h45 ")
elif idade >= 30 and idade < 40:
    print(" Seu horario é as 11h00 ")
else:
    print(" Você esta livre ")
