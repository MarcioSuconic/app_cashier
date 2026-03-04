from utils_banco_dados.conexao import Conexao

conexao = Conexao()

class Criacao_BD_Caixas:

    def __init__(self):
        self.conexao = conexao
        self.segue_o_fluxo()

    def segue_o_fluxo(self):
        self.retorna_dia_mes_ano_hoje()
        self.retorna_ultimo_caixa_criado()
        self.dif_dias_a_fazer_caixas()
        self.datas_a_criar()
        self.criar_caixa_padrao_e_dados_caixa()

    def retorna_dia_mes_ano_hoje(self):
        from app.utilitarios.datas.retornos_formatos_datas import entra_data_dt_retorna_data_sql
        from datetime import datetime
        self.hoje_dt = datetime.now().date()
        self.dia = self.hoje_dt.day
        self.mes = self.hoje_dt.month
        self.ano = self.hoje_dt.year
        self.hoje_str = entra_data_dt_retorna_data_sql(self.hoje_dt)
    
    def retorna_ultimo_caixa_criado(self):
        from app.utilitarios.datas.retornos_formatos_datas import return_dt_entry_sql

        sql = "SELECT max(`data_caixa`) FROM dados_fechamentos_caixa;"
        self.data_sql_max_caixa_criado_sql = self.conexao.bd_fetchall(sql)[0][0]
        self.data_sql_max_caixa_criado_dt = return_dt_entry_sql(self.data_sql_max_caixa_criado_sql)

    def dif_dias_a_fazer_caixas(self):
        self.dif_dias = (self.hoje_dt - self.data_sql_max_caixa_criado_dt).days

    def datas_a_criar(self):
        from datetime import timedelta

        self.lista_datas_a_criar = []

        for n in range(1, self.dif_dias+1):
            dif_dias = timedelta(days=n)            
            self.lista_datas_a_criar.append(dif_dias+self.data_sql_max_caixa_criado_dt)            

    def criar_caixa_padrao_e_dados_caixa(self):
        from app.utilitarios.utilitarios import proximo_id_dados_fechamento_caixa

        for data in self.lista_datas_a_criar:

            novo_id = proximo_id_dados_fechamento_caixa()

            comand = f"INSERT INTO dados_fechamentos_caixa (id, data_caixa, data_fechamento, usuario_id, resultado_final_cx, troco_final_cx, estoque_troco_cx, vendas_total, vendas_dinheiro_dia, vendas_pix_direto_cnpj, vendas_pix_direto_cpf, vendas_operadoras_maq_cartao, caixa_fechado) VALUES ({novo_id}, '{data}', '2024-07-31', 4, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0)"
            self.conexao.bd_commit(comand)        

            print(f"Caixa de {data} criado sob o ID {novo_id}.")
