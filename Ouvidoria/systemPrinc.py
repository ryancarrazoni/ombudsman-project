from Atalhos import *
from MySql.operacoesbd import *
abrirBD = abrirBancoDados('localhost', 'root', '1514131211', 'ouvidoria')
validar = Validacao()
formatar = Formatacao()
opcao = 0 
tipos = 'Sugestão', 'Reclamação', 'Elogio'
formatar.cabecalho('OUVIDORIA ABC')
while True:
    opcao = formatar.menu(['Listar todas as manifestações', 'Listar todas as sugestões', 'Listar todas as reclamações', 'Listar todas os elogios', 'Criar nova manifestação', 'Pesquisar por protocolo por ID', 'Sair'])
    if opcao == 1: #Mostrar todas as manifestações disponíveis.
        formatar.cabecalho('Manifestações:')
        codigoSQL = 'Select * from manifestos'
        listarSQL = listarBancoDados(abrirBD, codigoSQL)
        for listBDD in listarSQL:
            listartotal ='Protocolo' + ' - ' + str(listBDD[0])+ ' - ' + listBDD[1] + ' - '+ listBDD[2] + ' - ' + listBDD[3]
            print(listartotal)
        print(formatar.linha())
    elif opcao == 2: #Mostrar sugestões as disponiveís.
        formatar.cabecalho('Sugestões:')
        codigoSQL = 'Select * from manifestos where Tipo = "Sugestão"'
        listarSQL = listarBancoDados(abrirBD, codigoSQL)
        for listBDD in listarSQL:
            listartotal = 'Protocolo ' + ' - ' + str(listBDD[0]) + ' - ' + listBDD[1] + ' - ' + listBDD[3]
            print(listartotal)
        print(formatar.linha())
    elif opcao == 3: #Mostrar todas as reclamações.
        formatar.cabecalho('Reclamações:')
        codigoSQL = 'Select * from manifestos where Tipo = "Reclamação"'
        listarSQL = listarBancoDados(abrirBD, codigoSQL)
        for listBDD in listarSQL:
            listartotal = 'Protocolo' + ' - ' + str(listBDD[0]) + ' - ' + listBDD[1] + ' - ' + listBDD[3]
            print(listartotal)
        print(formatar.linha())
    elif opcao == 4: #Mostrar todos os elogios.
        formatar.cabecalho('Elogios:')
        codigoSQL = 'Select * from manifestos where Tipo = "Elogio"'
        listarSQL = listarBancoDados(abrirBD, codigoSQL)
        for listBDD in listarSQL:
            listartotal = 'Protocolo' + ' - ' + str(listBDD[0]) + ' - ' + listBDD[1] + ' - ' + listBDD[3]
            print(listartotal)
        print(formatar.linha())    
    elif opcao == 5: #Enviar nova manifestação conforme seu tipo.
        tipo = 0
        nome = validar.leianome('\033[32mRequisitante: \033[m')
        while tipo < 1 or tipo > 3:
            tipo = formatar.menu(['Sugestão', 'Reclamação', 'Elogio'])
            if tipo < 1 or tipo > 3: #Menor que 1 ou maiores que 3 ==> Opção inválida.
                print('Opção inválida!')
        descricao = validar.leianome('\033[32mDigite seu manifesto: \033[m')
        print(formatar.linha())
        sql = "INSERT INTO manifestos(Nome,Tipo,Descricao) VALUES (%s, %s, %s)"
        dados = (nome, tipos[tipo - 1], descricao)
        insertNoBancoDados(abrirBD,sql,dados)
    elif opcao == 6: #Pesquisar manifetações por número(ID).
        numeroprot = -1
        manifestacoes = 'select protocolo from manifestos'
        protocolo = listarBancoDados(abrirBD, manifestacoes)
        tamprotocolo = len(protocolo)
        while numeroprot <= 0 or numeroprot > tamprotocolo: 
            numeroprot = validar.leiaint('Informe o número do protocolo: ') #Pesquisar manifestação por número.
            if numeroprot <= 0 or numeroprot > tamprotocolo: #Menor ou igual 0, ou maior que o tamanho do protocolo imprime o print.
                print('Número do protolo inválido, consulte-o novamente!')
                break
        pesqprotocolo = 'Select * from manifestos where Protocolo='+str(numeroprot)
        listarSQL = listarBancoDados(abrirBD, pesqprotocolo)
        for listBDD in listarSQL:
            listartotal = 'Protocolo ' + ' - ' + str(listBDD[0]) + ' - ' + listBDD[1] + ' - ' + listBDD[2] + ' - ' + listBDD[3]
            print(listartotal) 
        print(formatar.linha())
    elif opcao == 7:
        print('Saindo...')
        break
encerrarBancoDados(abrirBD)