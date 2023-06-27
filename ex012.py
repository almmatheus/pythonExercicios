prec = float(input('Qual é o preço do produto? R$'))
desc = prec - (prec * 5 / 100)
print(f'O produto que custava R${prec}, na promoção com desconto de 5% vai custar R${desc:.2f}')
