import random

condicional simples

chute_aleatorio = random.randint(1,2)
if chute_aleatorio == 2:
    print('acertei', chute_aleatorio)

condicional composta


aleatorio =  random.randint(1,2)
meu_chute = int(input('Digite seu chute: '))

#condição verdadeira
if meu_chute <= aleatorio:
   print(aleatorio + meu_chute) 
   print('Show de bola!', aleatorio)
# codição falsa    
else:
    print('Errou feio', aleatorio)   

senha_aleatoria = random.randint(10000,20000)

minha_senha = int(input('Digite sua senha '))
if minha_senha == senha_aleatoria:
    print('Acesso liberado', senha_aleatoria)
elif minha_senha >= senha_aleatoria:
    print('Esta quase acertando', senha_aleatoria)
else:
    print('Senha incorreta, tente novamente', senha_aleatoria)



                