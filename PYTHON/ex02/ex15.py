nome=input('Digite o seu nome: ')
salario=float(input('Digite o valor do salário: '))
aumento=float(input("Digite o valor do aumento: "))

salario_desconto= salario * (aumento/100)
salario_novo= salario_desconto + salario

print('O valor final do salário será de: ' ,salario_novo)