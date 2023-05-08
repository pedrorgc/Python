dhm= input(('Digite a quantidade de dias, horas, minutos e segundos no formato DD-HH-MM-SS: '))
dias, horas, minutos, seg= map(int, dhm.split("-"))
segd= dias*86400
segh= horas*3600
segm= minutos*60
segt= segd+segh+segm

print('O total em segundos será de: ' ,segt)