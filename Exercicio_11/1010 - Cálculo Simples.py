#Beecrowd

#Neste problema, deve-se ler o código de uma peça 1,
#o número de peças 1, o valor unitário de cada peça 1, 
#o código de uma peça 2, o número de peças 2 e o valor 
#unitário de cada peça 2. Após, calcule e mostre o valor 
#a ser pago.

#Entrada
#O arquivo de entrada contém duas linhas de dados. 
#Em cada linha haverá 3 valores, respectivamente dois 
#inteiros e um valor com 2 casas decimais.

#Saída
#A saída deverá ser uma mensagem conforme o exemplo 
#fornecido abaixo, lembrando de deixar um espaço após os 
# dois pontos e um espaço após o "R$". 
#O valor deverá ser apresentado com 2 casas após o ponto.

#Resolução
# Lendo os dados da primeira peça
Cod_peca1, num_pca1, valor_peca1 = input().split()
num_pca1 = int(num_pca1)  # Convertendo para inteiro
valor_peca1 = float(valor_peca1)  # Convertendo para float

# Lendo os dados da segunda peça
Cod_peca2, num_pca2, valor_peca2 = input().split()
num_pca2 = int(num_pca2)  # Convertendo para inteiro
valor_peca2 = float(valor_peca2)  # Convertendo para float

# Calculando o valor a pagar para as duas peças
valor_a_paga1 = valor_peca1 * num_pca1
valor_a_paga2 = valor_peca2 * num_pca2

# Calculando o valor total a pagar
total = valor_a_paga1 + valor_a_paga2

# Exibindo o valor total formatado
print('VALOR A PAGAR: R$ {:.2f}'.format(total))
