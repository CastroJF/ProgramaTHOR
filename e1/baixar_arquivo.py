import requests
import csv

class BaixarArquivo:
    _ARQUIVO_URL_BASE = "http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_"
    _ARQUIVO_EXTENSAO = ".csv"
    _nomeArquivo = None

    def __init__(self, nomeArquivo):
        self._setNomeArquivo(nomeArquivo)


    def obterUrl(self):
        return self._ARQUIVO_URL_BASE + self._nomeArquivo + self._ARQUIVO_EXTENSAO

    def _setNomeArquivo(self,nomeArquivo):
        if(type(nomeArquivo) != str):
            return None

        self._nomeArquivo = nomeArquivo

    def baixarArquivo(self):
        r = requests.get(self.obterUrl())

        if (r.status_code == 404):
            return 404

        return r.content