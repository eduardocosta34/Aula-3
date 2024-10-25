a = int(input('Numero um: '))
b = int(input('Numero dois: '))
c = int(input('Numereo três: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O menor valor digitado foi: {menor}')
print(f'O maior valor digitado foi: {maior}')