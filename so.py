import random


so = ['Estados Unidos', 'Brasil', 'Inglaterra', 'Espanha', 'Japão', 'China',
    'Russia', 'Alemanha']

#print(random.choice(so))

random.shuffle(so)
for tarefa in so:
    print(tarefa)

