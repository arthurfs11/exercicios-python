import random #IMPORTAMOS O MÓDULO RAMDOM PARA GERAR O NÚMERO ALEATÓRIO

numero_aleatorio = random.randint(1, 10) #O COMPUTADOR GERA UM NÚMERO ALEATÓRIO ENTRE 1 E 10
tentativas = 0 #CONTAGEM DE QUANTAS TENTATIVAS O USUÁRIO LEVOU PARA ACERTAR, SEMPRE INICIA EM 0 TENTATIVAS

print("Olá! Duvido você acertar meu número secreto entre 1 em 10...") #SAUDAÇÃO DO PROGRAMA COM O DESAFIO

while True: #ENQUANTO A CONDIÇÃO FOR VERDADEIRA (OU SEJA, ENQUANTO O USUÁRIO NÃO ACERTAR O NÚMERO)
    try: #AQUI USAMOS A ESTRUTURA DE TRY EXCEPT, PARA EVITAR QUE O USUÁRIO DIGITE VALORES INVÁLIDOS
        palpite = int(input("Digite seu palpite: ")) #AQUI PERGUNTAMOS O PALPITE E SALVAMOS NA VARIÁVEL PALPITE
        tentativas += 1 #ATRIBUÍMOS +1 PARA CADA PALPITE QUE O USUÁRIO DIGITAR PARA CONTABILIZAR O NÚMERO DE TENTATIVAS

        if palpite < 1 or palpite > 10: #AQUI AVALIAMOS SE O NÚMERO DIGITADO ATENDE A REGRA DE ESTAR ENTRE 1 E 10
            print("Por favor, digite um número entre 1 e 10.") #SE O NÚMERO FOR MENOR QUE 1 OU MAIOR QUE 10, O PROGRAMA PEDE PARA QUE O USUÁRIO DIGITE APENAS NÚMEROS DE 1 A 10
            continue #E ENTÃO, SEGUE PARA A PRÓXIMA ITERAÇÃO DESTE LOOP

        if palpite == numero_aleatorio: #SE O PALPITE FOR O NÚMERO SECRETO:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.") #PARABENIZA O USUÁRIO E DIZ QUE ACERTOU EM X TENTATIVAS
            break #ENCERRA FLUXO NO COMANDO BREAK
        elif palpite < numero_aleatorio: #SE O PALPITE FOR MENOR QUE O NUMERO SECRETO:
            print("O número é maior. Tente novamente.") #INFORMA QUE O NÚMERO SECRETO É MENOR:
        else: #SE O NÚMERO NÃO FOR IGUAL E NÃO FOR MENOR, POR FIM SERÁ MAIOR, ENTÃO EXIBE A MENSAGEM:
            print("O número é menor. Tente novamente.") #INFORMA QUE O NÚMERO É MAIOR.

    except ValueError: #EXCEPT CONCENTRA TODOS OS ERROS DE PROCESSO
            print("Por favor, digite apenas números.") #INFORMA QUE SÃO ACEITOS APENAS NÚMEROS