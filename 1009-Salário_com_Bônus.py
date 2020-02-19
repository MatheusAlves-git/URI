nome = str(input())
salario = float(input())
totvenda = float(input())
total = (totvenda*15)/100 + salario
print('TOTAL = R$ {:.2f}'.format(total))