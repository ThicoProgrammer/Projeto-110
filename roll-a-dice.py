import random

resposta = 'S'

while resposta == 'S':
    numero = random.randint(1,6)

    if numero == 1:
        print('[-----]')
        print('[     ]')
        print('[  o  ]')
        print('[     ]')
        print('[-----]')

    if numero == 2:
        print('[-----]')
        print('[ o   ]')
        print('[     ]')
        print('[   o ]')
        print('[-----]')

    if numero == 3:
        print('[-----]')
        print('[ o   ]')
        print('[  o  ]')
        print('[   o ]')
        print('[-----]')

    if numero == 4:
        print('[-----]')
        print('[ o o ]')
        print('[     ]')
        print('[ o o ]')
        print('[-----]')

    if numero == 5:
        print('[-----]')
        print('[ o o ]')
        print('[  o  ]')
        print('[ o o ]')
        print('[-----]')

    if numero == 6:
        print('[-----]')
        print('[ o o ]')
        print('[ o o ]')
        print('[ o o ]')
        print('[-----]')

    resposta = input('Pressione S para jogar novamente e N para sair: ')
    print('\n')