from e1.e1 import E1
from e2.e2 import *
arquivos = []
while True:
    print('\n\nArquivo a Ser Baixado: ')
    escolha = input("Pressione enter para continuar\nSe dejar sair pressionce 0 + enter\n::: ")

    if(escolha == "0"):
        break

    arquivos.append(E1().verArquivoPath())

cnpjs = input("\n\nDigite os cnpjs separados por virgula, ou deixe em branco para selecionar todos(Pode demorar um pouco)\n::: ")
e2 = E2(arquivos, cnpjs.split(','))
print(e2.relatorio())