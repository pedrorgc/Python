print('!!!!Diferença de Preço!!!!')
etanol=float(input('Digite o valor do etanol: '))
gasolina=float(input('Digite o valor do álcool: '))

menor_valor= min(etanol, gasolina)
maior_valor= max(etanol, gasolina)

diferenca= maior_valor - menor_valor
div= diferenca/menor_valor
percentual= div * 100

print(f"O percentual de proporção entre {menor_valor} e {maior_valor} é de {percentual:.2f}%")