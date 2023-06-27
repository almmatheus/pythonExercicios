import math
ang = float(input('Digite o ângulo que você deseja: '))
se = math.sin(math.radians(ang))
co = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'O ângulo de {ang} tem o SENO de {se:.2f}')
print(f'O ângulo de {ang} tem o COSSENO de {co:.2f}')
print(f'O ângulo de {ang} tem a TANGENTE de {tan:.2f}')
