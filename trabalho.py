import math

#execicio 1 

raio = float(input("Digite o valor do raio da esfera (R): "))
volume = (4/3) * math.pi * raio**3
print(f"O volume da esfera com raio {raio} é: {volume:.2f}")

# exercicio 2

peso= float(input("qual é o seu peso?"))
resultado = peso * 0.3
print(resultado)

#exercicio 3 

x1 = float(input("Digite a coordenada x do primeiro ponto: "))
y1 = float(input("Digite a coordenada y do primeiro ponto: "))

x2 = float(input("Digite a coordenada x do segundo ponto: "))
y2 = float(input("Digite a coordenada y do segundo ponto: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"A distância entre os pontos é {distancia:.2f}")

# exercicio 4

valor1 = int(input("digite o valor1:"))
valor2 = int(input("digite o valor2:"))

if valor1 < valor2:
   print(f"os valores em ordem crescente são: {valor1} e {valor2}")
else:
   print(f"os valores em ordem crescente são: {valor2} e {valor1}")

#exercicio 5

altura_homem = float(input("digite a altura do homem:"))
altura_mulher = float(input("digite a alttura da mulher:"))

peso_para_homem = (72.7 * altura_homem) - 58
peso_para_mulher = (62.1 * altura_mulher) - 44.7

print(f"o peso ideal para um homem de acordo com sua altura é {altura_homem} e {peso_para_homem:.2f}")
print(f"o peso ideal para um homem de acordo com sua altura é {altura_mulher} e {peso_para_mulher:.2f}")

print("Exercicios concluidos")