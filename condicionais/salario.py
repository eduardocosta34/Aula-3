salario = float(input('QUal o salário do funcionário: R$ '))
if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

print(f'o aumento vai ser de R$ {aumento:.2f} - novo salário de: R$ {salario + aumento:.2f}')