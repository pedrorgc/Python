data= input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data.split('/')
nova_data= ano + '/' + mes + '/' + dia
print ("Nova data:" ,nova_data)