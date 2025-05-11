
numeros= 0
soma = 0
valores_maiores_que_20 = 0

while True:
    valor = float(input("digite um valor real ou 0 para acabar com o loop: "))
    if valor == 0:
        break
    numeros += 1
    soma += valor

    if valor > 20:
       valores_maiores_que_20 += 1

if numeros > 0:
    media = soma / numeros
    print(f"quantidade de valores digitados: {numeros}")
    print(f"soma dos valores digitados: {soma}")
    print(f"média aritmética dos valores digitados: {media: .2f}")
    print(f"quantidade de valores maiores que 20: {valores_maiores_que_20}")
    print("nenhum valor foi digitado")

# exercicio 2 

alunos_aprovados = 0
alunos_reprovados = 0
total_de_alunos = 0

while True:
    nota = float(input("digite a nota do aluno ou -1 para acabar o loop: "))

    if nota == -1:
        break
    total_de_alunos += 1
  
    if nota >= 5:
      alunos_aprovados += 1
    else:
      alunos_reprovados += 1 
    
if total_de_alunos > 0:
      
    print(f"quantidade de alunos digitados: {total_de_alunos}")
    print(f"quantidade de alunos que foram aprovados: {alunos_aprovados}")
    print(f"quantidade de alunos que foram reprovados: {alunos_reprovados}")
else:
    print("sem nota, pois sem aluno digitado")

provados = 0
reprovados = 0
quantidade_alunos = 0

#exercicio 3 

pares = impares = soma_pares = soma_impares = 0

while True:
    numero = int(input("digite um numero ou 0 para acabar o loop: "))

    if numero == 0:
        break

    if numero % 2 == 0:
        soma_pares += numero
        pares += 1
    else:
        soma_impares += numero
        impares += 1

if pares > 0:
    media_pares = soma_pares / pares
else:
    media_pares = 0

if impares > 0:
    media_impares = soma_impares / impares
else:
    media_impares = 0

print(f"Média dos números pares: {media_pares:.2f}")
print(f"Média dos números ímpares: {media_impares: .2f}")

#exercicio 4 

def este_exercicio_foi_criado_a_mais_para_o_vs_code_nao_bugar(altura, largura):
  resultado = altura * largura
  return (resultado)

print(este_exercicio_foi_criado_a_mais_para_o_vs_code_nao_bugar(8, 10))