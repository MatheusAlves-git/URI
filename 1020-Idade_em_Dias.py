idade = int(input())
ano = idade//365
mes = ano % idade
dia = (idade%365)%30
print(ano)
print(mes)
print(dia)