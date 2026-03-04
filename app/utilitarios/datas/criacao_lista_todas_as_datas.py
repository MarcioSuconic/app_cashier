class Criacao_Lista_Todas_Datas:

    def __init__(self, conexao, modo_procura):
        self.conexao = conexao
        self.modo_procura = modo_procura
        self.segue_o_fluxo()

    def segue_o_fluxo(self):        
        self.define_data_atual()
        self.verificacao_datas_ja_feitas()
        self.criacao_lista_datas()

    def define_data_atual(self):
        from datetime import datetime
        data_atual = datetime.now()
        self.data_atual = data_atual.date()

    def verificacao_datas_ja_feitas(self):

        self.lista_ja_verificada = []

        if self.modo_procura == 'vendas':
            sql = "SELECT fecham.data_fechamento_sql FROM marsoft.msf_mot_motores_diarios as mot inner join marsoft.msf_fcx_fechamentos_caixas_dia as fecham on mot.`fechamento_caixa_id` = fecham.`id` WHERE mot.`vendas_diaria_lida` = '1';"
            resultado = self.conexao.executa_DQL(sql)

            for result in resultado:
                self.lista_ja_verificada.append(result[0])

    def criacao_lista_datas(self):
        from datetime import datetime, timedelta
        self.data_inicial = datetime(day=1,month=8,year=2024)
        diferencas_datas = self.data_atual - self.data_inicial.date()
        self.lista_todas_datas = []

        for n in range(0, int(diferencas_datas.days)+1):
            delta_dias = timedelta(days=n)
            data_leitura = (self.data_inicial + delta_dias).date()

            if data_leitura not in self.lista_ja_verificada:
                self.lista_todas_datas.append(data_leitura)               

    def retorna_a_lista_todas_datas(self):
        return self.lista_todas_datas
