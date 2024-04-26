lista_mercado = ['Arroz', 'Feijão', 'Suco', 'Carne'] #CRIAÇÃO DA LISTA COM OS PARÂMETROS INICIAIS

for i in lista_mercado: #LOOP QUE SERÁ REPETIDO PARA CADA ITEM CONTIDO NA LISTA "LISTA MERCADO"
    novo_produto = str(input('Qual produto você está comprando?')) #PERGUNTA AO USUÁRIO O PRODUTO QUE ESTÁ SENDO COMPRADO
    if novo_produto in lista_mercado: #SE O NOVO PRODUTO EXISTIR NA LISTA DO MERCADO, SEGUE NA LINHA 6, SE NÃO, LINHA 8
        print(f'Produto {novo_produto} já está na lista!') #EXIBE QUE NOVO PRODUTO JÁ ESTÁ NA LISTA
        continue #SEGUE PARA PRÓXIMO ITEM DA LISTA
    else: #SE O NOVO PRODUTO NÃO EXISTIR NA LISTA
        lista_mercado.append(novo_produto) #ADICIONA O NOVO PRODUTO A LISTA
        print(f'Produto {novo_produto} ascrescentado à lista do mercado.') #EXIBE QUE O NOVO PRODUTO FOI ADICIONADO A LISTA
        continue #SEGUE PARA PRÓXIMO ITEM DA LISTA