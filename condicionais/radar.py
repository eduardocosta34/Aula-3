velocidade = float(input('Velocidade do carro: '))
print(f'Velocidade do carro: {velocidade}Km/h')
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'você foi multado, valor a pagar: R$ {multa:.2f}')
else:
    print('Está dentro da velocidade permitida')
