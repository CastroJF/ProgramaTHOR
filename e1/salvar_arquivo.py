import os
class SalvarArquivo:
    _csv_arquivo_string = None
    _diretorio = None

    def __init__(self, csv_arquivo_string):
        self._csv_arquivo_string = csv_arquivo_string

    def salvar(self, diretorio, nome):
        nomeArquivo = ""
        if(diretorio[-1]=="/"):
            nomeArquivo = ""+nome+".csv"
        else:
            nomeArquivo = "/"+nome+".csv"

        if not os.path.exists(diretorio):
            os.makedirs(diretorio)

        self._diretorio = diretorio+nomeArquivo
        with open(self._diretorio, 'wb') as arquivo:
            arquivo.write(self._csv_arquivo_string)
            arquivo.close()

    def verDiretorio(self):
        return self._diretorio