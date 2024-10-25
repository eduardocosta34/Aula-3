distancia = float(input('Distancia da viagem em Kms: '))

valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print(f'A sua viagem de {distancia} Kms - Valor de R$ {valor:.2f}')

# if distancia <= 200:
#     valor = distancia * 0.50
#     print(f'A sua viagem de {distancia} Kms - valor de R$ {valor}')
# else:
#     valor = distancia * 0.45
#     print(f'A sua viagem de {distancia} Kms - valor promocional de R$ {valor}')