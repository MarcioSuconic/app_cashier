class Criacao_Pastas_Mes_x_Ano:

    def __init__(self):
        self.__follow_the_flow()

    def __follow_the_flow(self):
        self.__date_now()
        self.__exists_path()

    def __date_now(self):
        from datetime import datetime, timedelta
        from app.utilitarios.datas.retornos_formatos_datas import entra_data_dt_retorna_data_sql
        from app.utilitarios.datas.retornos_partes_da_data import retorna_ano_data_str, retorna_mes_data_str

        agora = datetime.now()

        mes_atual = agora.month
        ano_atual = agora.year

        lista_meses = ['01','02','03','04','05','06','07','08','09','10','11','12']
        lista_anos = [f'{ano_atual}',f'{ano_atual+1}']

        self.list_months = []
        self.list_years = []

        for n in [0,1,2,3]:

            pos_mes = mes_atual - 1 + n
            pos_ano = 0

            if pos_mes >= 12:
                pos_mes -= 12
                pos_ano += 1

            self.list_months.append(str(lista_meses[pos_mes]))
            self.list_years.append(str(lista_anos[pos_ano]))

    def __exists_path(self):
        from pathlib import Path
        from app.utilitarios.arquivos.pastas import verifica_se_caminho_existe
        from datetime import datetime

        path_dir = Path().absolute()
       
        for i in [0,1,2,3]:

            self.caminho_estoque = Path(path_dir).joinpath('arquivos_excel_sistema_euro').joinpath(f'{self.list_years[i]}').joinpath(f'{self.list_months[i]}').joinpath('estoque')
            self.caminho_vendas = Path(path_dir).joinpath('arquivos_excel_sistema_euro').joinpath(f'{self.list_years[i]}').joinpath(f'{self.list_months[i]}').joinpath('vendas')

            existe_caminho_estoque = self.caminho_estoque.exists()
            existe_caminho_vendas = self.caminho_vendas.exists()

            if existe_caminho_estoque == False:
                self.__create_path(self.caminho_estoque)

            if existe_caminho_vendas == False:
                self.__create_path(self.caminho_vendas)

    def __create_path(self, caminho):
        caminho.mkdir(parents=True, exist_ok=True)

