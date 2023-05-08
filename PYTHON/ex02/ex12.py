salario_minimo = float(input("Digite o valor do salário mínimo: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
valor_hora = salario_minimo / 5
salario_bruto = horas_trabalhadas * valor_hora
desconto = salario_bruto * 0.1
salario_liquido = salario_bruto - desconto
print("Salário bruto:", salario_bruto)
print("Salário líquido:", salario_liquido)