import csv


class E2:
    _arquivoPath = []
    _arquivos = []
    _cnpjs = []
    _cnpjRegistros = {}

    def __init__(self, arquivoPath, cnpjs):
        self._arquivoPath = arquivoPath
        self.abrirArquivos(arquivoPath)
        self._cnpjs = cnpjs

        if len(cnpjs) == 0:
            print('listando todos cnpjs')
            self.listarTodosCnpjs()
            print('terminou de listar todos cnpjs')
        self.listarPorCnpj()

    def abrirArquivos(self, arquivoPath):
        for arquivo_nome in arquivoPath:
            self._arquivos.append(csv.reader(open(arquivo_nome, newline='')))

    def listarTodosCnpjs(self):
        for arquivo in self._arquivos:
            for row in arquivo:
                colunas = row[0].split(';')
                cnpjRow = colunas[0]
                if cnpjRow != "CNPJ_FUNDO":
                    if cnpjRow not in self._cnpjs:
                        self._cnpjs.append(cnpjRow)

    def listarPorCnpj(self):
        self._cnpjRegistros = {}
        for cnpj in self._cnpjs:
            self._cnpjRegistros[cnpj] = []

        for arquivo in self._arquivos:
            for row in arquivo:
                colunas = row[0].split(';')
                cnpjRow = colunas[0]
                for cnpj in self._cnpjs:
                    if (cnpj == cnpjRow):
                        self._cnpjRegistros[cnpj].append(
                            {'dtComptc': colunas[1], 'vl_quota': int(float(colunas[3].replace('.', ''))), 'capt_dia': colunas[5],
                             'resg_dia': colunas[6]})

    def relatorio(self):
        for cnpj in self._cnpjRegistros.keys():
            try:
                ultimoValor = self._cnpjRegistros[cnpj][0]['vl_quota']
                for registro in self._cnpjRegistros[cnpj]:
                    if (registro == None):
                        continue
                    # M = C(1+i)->i=M/C -1 | Montante = Capital(1 + taxa) -> taxa = Montante/Capital - 1 | formula usada para calcular a variação
                    print("CNPJ: " + cnpj + "\tData: " + registro['dtComptc'] + "\tVariação: " + str(
                        round((registro['vl_quota'] / ultimoValor - 1) * 100, 4)) + "%\tValor Captado" + registro[
                              'capt_dia'] + "\tValor Resgatado: " + registro["resg_dia"])
                    ultimoValor = registro['vl_quota']
            except IndexError:
                pass
