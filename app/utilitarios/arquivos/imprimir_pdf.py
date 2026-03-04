class Imprimir_pdf:

    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.nome_impressora = None
        self.__verifica_se_caminho_existe()
        self.__define_impressora()

    def __define_impressora(self):

        import win32print

        if self.nome_impressora == None:
            self.nome_impressora = win32print.GetDefaultPrinter()

    def imprimir_pdf(self):
        import os
        self.comando = f'print /d:"{self.nome_impressora}" "{self.caminho_arquivo}"'
        
        if self.nome_impressora != None:
            if self.exist_file:
                os.system(self.comando)

    def __verifica_se_caminho_existe(self):
        from utilitarios.arquivos.arquivos import verifica_se_arquivo_existe
        self.exist_file = verifica_se_arquivo_existe(self.caminho_arquivo)
    