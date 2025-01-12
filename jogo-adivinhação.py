numero_correto = 7
tentativas = 0

print('Bem-vindo! Nesse jogo, você terá 3 chances para adivinhar o número correto de 1-10.')

while tentativas < 3:  
    palpite = int(input(f'Digite a sua {tentativas + 1}ª tentativa: '))

    if 1 <= palpite <= 10:  
        tentativas += 1

        if palpite == numero_correto:
            print('Parabéns! Você adivinhou o número correto.')
            break
    else:
        print('Erro. Digite um número de 1-10.')
else:
    print(f'Foi quase! O número correto era {numero_correto}.')