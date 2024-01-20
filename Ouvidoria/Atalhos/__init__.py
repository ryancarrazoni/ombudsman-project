class Validacao:
    def leiaint(self, txt):
        while True:
            try:
                numero = int(input(txt))
            except (ValueError ,TypeError, KeyboardInterrupt):
                print('\033[31mErro: Insira um número inteiro.\033[m')
            else:
                return numero
                
    def leianome(self, txt):
        while True:
            try:
                nome = str(input(txt))
            except (ValueError ,TypeError, KeyboardInterrupt):
                print('\033{31mErro: Insira um nome válido.\033[m')
            else:
                return nome
class Formatacao: 
    def linha(self, tamanho=100):
        return '=' * tamanho

    def cabecalho(self, txt):
        print('='*100)
        print(txt.center(100))
        print('='*100)

    def menu(self, lista):
        vali = Validacao()
        contador = 1
        for itens in lista:
            print(f'\033[33m{contador})\033[m \033[34m{itens}\033[m')
            contador += 1
        print('='*100)
        opcao = vali.leiaint('\033[32mSua opção: \033[m')
        return opcao
