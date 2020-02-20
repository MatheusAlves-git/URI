cod_peca1, quant_peca1, valoruni_peca1 = input().split()

cod_peca2, quant_peca2, valoruni_peca2 = input().split()

valor = float(valoruni_peca1)*int(quant_peca1)+float(valoruni_peca2)*int(quant_peca2)
print('VALOR A PAGAR: R$ {:.2f}'.format(valor))
