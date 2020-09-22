from e1.baixar_arquivo import BaixarArquivo
from e1.salvar_arquivo import SalvarArquivo

class E1:
    _arquivo_path = None

    def __init__(self):
        print("Olá, seja bem vindo, por favor entre com os dados necessários para baixar o arquivo csv")
        while True:
            nomeArquivo = input('Entre com o mes e o ano neste formato: YYYYMM ::: ') #201701

            if(self.validarNomeArquivo(nomeArquivo)==None):
                continue

            baixarArquivo = BaixarArquivo(nomeArquivo)
            arquivo = baixarArquivo.baixarArquivo()

            if arquivo == 404:
                print('Arquivo Não Encontrado')
                exit()

            diretorio = input('Selecione o diretorio a ser salvo ::: ')

            salvarArquivo = SalvarArquivo(arquivo)
            salvarArquivo.salvar(diretorio, nomeArquivo)

            self._arquivo_path = salvarArquivo.verDiretorio()
            return

    def validarNomeArquivo(self, nome):
        if (nome.__len__() == 6):
            if (int(nome[4:6]) > 0 and int(nome[4:6]) < 13):
                return 'ok'
            else:
                print('Mês invalido')
                return None
        else:
            print('Por favor, a data deve ser escrica como YYYYMM')
            return None

    def verArquivoPath(self):
        return self._arquivo_path