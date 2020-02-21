A, B, C = input().split()
retangulo = float(A)*float(B)
quadrado = float(B)*float(B)
trapezio = ((float(B)+float(A))*float(C))/2
circulo = float(C)**2 * 3.14159
triangulo = float(A)*float(C)/2
print('TRIANGULO: {:.3f}'.format(triangulo))
print('CIRCULO: {:.3f}'.format(circulo))
print('TRAPEZIO: {:.3f}'.format(trapezio))
print('QUADRADO: {:.3f}'.format(quadrado))
print('RETANGULO: {:.3f}'.format(retangulo))

