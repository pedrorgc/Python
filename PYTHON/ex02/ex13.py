preco=float(input('Digite o preço do produto: '))
desconto=float(input('Digite o valor do desconto: '))

valor_desconto= preco * (desconto/100)
valor_final= valor_desconto - preco


print('O valor com desconto: ' ,valor_desconto)
print('O valor final será de: ' ,valor_final)