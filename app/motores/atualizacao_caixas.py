class Atualizacao_BD_Caixas:

    def __init__(self):
        self.atualiza()

    def atualiza(self):
        from utils_banco_dados.conexao import Conexao

        conexao = Conexao()

        # command = "UPDATE dados_fechamentos_caixa SET data_caixa = '2025-11-13', data_fechamento='2025-12-16', hora=18, minutos=13, caixa_fechado = 1, read_app_parent = 0, usuario_id = 4, resultado_final_cx = -0.02, troco_final_cx=815.1, estoque_troco_cx=100.0, vendas_total=3160.22, vendas_dinheiro_dia=0.02, vendas_pix_direto=0.0, vendas_operadoras_maq_cartao=3160.2, result_trocas_devs_dinheiro=0.0, result_trocas_devs_debito=0.0, result_trocas_devs_credito=0.0, result_trocas_devs_produtos=0.0 WHERE id = 471;"
        # conexao.bd_commit(command)

        # command = ""
        # conexao.bd_commit(command)

        # command = ""
        # conexao.bd_commit(command)

        # command = ""
        # conexao.bd_commit(command)

        # command = ""
        # conexao.bd_commit(command)