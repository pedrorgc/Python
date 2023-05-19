valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

menor_valor = min(valor1, valor2)
maior_valor = max(valor1, valor2)

diferenca = maior_valor - menor_valor
razao = diferenca / menor_valor
percentual = razao * 100

print(f"O percentual de proporção entre {menor_valor} e {maior_valor} é de {percentual:.2f}%")
