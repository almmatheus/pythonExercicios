import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
Lista = [a1, a2, a3, a4]
esc = random.choice(Lista)
print(f'O aluno escolhido foi {esc}')
