from datetime import date #LIB PARA BUSCAR DATAS

ano = date.today().year #CRIAMOS A VARIÁVEL ANO PARA RETORNAR O ANO ATUAL, ASSIM NÃO PRECISA ATUALIZAR O CÓDIGO A CADA ANO

nome = str(input('Olá! Qual é o seu nome?')) #PERGUNTA O NOME DO USUÁRIO E SALVA NA VARIÁVEL NOME EM FORMATO STRING
idade = int(input('Quantos anos você tem?')) #PERGUNTA A IDADE DO USUÁRIO E SALVA NA VARIÁVEL IDADE EM FORMATO INTEIRO

ano_nascimento = (ano - idade) #CALCULA ANO DE NASCIMENTO MENOS A IDADE INFORMADA PELO USUÁRIO

print(f"Olá {nome}, você nasceu em {ano_nascimento}.") #RETORNA A SENTENÇA "OLÁ ,USUARIO, VOCÊ NASCEU EM ,ANO NASCIMENTO."