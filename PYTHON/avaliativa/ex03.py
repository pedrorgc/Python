valor=float(input('Digite o valor do produto: '))

if(valor <= 100.00):
  desconto= valor * (5/100)

elif(valor >=100 <=500):
    desconto= valor * (10/100)

else:(valor >500)
desconto= valor * (15/100)

preco_desconto= valor - desconto

print(f'O preço com desconto é {preco_desconto}')