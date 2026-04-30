import sys
import json
from pathlib import Path
import sqlite3  # Adicione esta importação
from qt_core import *
from gui.windows.main_window.ui_main_window import *
from utils_banco_dados.banco_dados import Banco_Dados

from app.motores.criacao_pastas_mes_x_ano import Criacao_Pastas_Mes_x_Ano
from app.motores.criacao_bd_caixas import Criacao_BD_Caixas
from app.motores.atualizacao_caixas import Atualizacao_BD_Caixas

from app.utilitarios.arquivos.pastas import exists_database_out

# MAIN WINDOW
class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
       
        self.name_user = ''
        self.choiced_date = False

        # first time
        self.verificador_first_time()

        # TITLE
        self.setWindowTitle("SISTEMA DE CAIXA")

        # BANCO DE DADOS
        #Banco_Dados()

        # criação de pastas para importação dos arquivos do Sistema Euro
        Criacao_Pastas_Mes_x_Ano()

        # criação de banco de dados para criação de novos caixas
        Criacao_BD_Caixas()

        # atualizacoes fechamentos caixas
        if self.first_time == True:
            Atualizacao_BD_Caixas()

        # existe a pasta database_out
        exists_database_out()

        # SETUP MAIN WINDOW
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # boas vindas antes de login
        self.ui.ui_pages.lbl_ola.hide()
        self.ui.ui_pages.btn_selection_date.hide()

        # botao LOGIN
        self.ui.ui_pages.btn_login.clicked.connect(self.login_button)
            
        # Toggle Button
        self.ui.btn_toggle.clicked.connect(self.toggle_button)

        # Troco Caixa Button
        self.ui.btn_troco_cx.clicked.connect(self.troco_caixa_button)

        # Fechamento Caixa Button
        self.ui.btn_fech_cx.clicked.connect(self.fechamento_caixa_button)

        # Escolha Data do Caixa
        self.ui.btn_data_cx.clicked.connect(self.escolha_data_cx_button)

        # botao repetir troco cx
        self.ui.ui_pages.btn_repetir_troco_cx.clicked.connect(self.repetir_troco_cx)

        # botao repetir estoque troco cx
        self.ui.ui_pages.btn_repetir_estoque_troco_cx.clicked.connect(self.repetir_estoque_troco_cx)

        # Entradas n Operadora Caixa
        self.ui.btn_entradas_n_operadora.clicked.connect(self.entrada_n_operadora_button)
        self.ui.ui_pages.btn_ver_entrada_n_operadora.clicked.connect(self.entrada_n_operadora_button)

        # Observação do Caixa
        self.ui.btn_obs_cx.clicked.connect(self.observacao_cx_button)
        self.ui.ui_pages.btn_ver_observacoes.clicked.connect(self.observacao_cx_button)

        # Trocas/Devoluções do Caixa
        self.ui.btn_trocas_devolucoes.clicked.connect(self.trocas_devolucoes_button)        
        self.ui.ui_pages.btn_ver_trocas_dev.clicked.connect(self.trocas_devolucoes_button)

        # Ver Despesas de Caixa
        self.ui.btn_despesas.clicked.connect(self.ver_despesas_cx_button)
        self.ui.ui_pages.btn_ver_despesas.clicked.connect(self.ver_despesas_cx_button)

        # ir para inserir despesa
        self.ui.ui_pages.btn_inserir_despesa_cx.clicked.connect(self.inserir_despesas_cx_button)

        # pagina fechamentos parciais caixa
        self.ui.ui_pages.btn_ver_fechamentos_parciais.clicked.connect(self.ver_fechamentos_parciais_cx)

        # Ver Data Escolhida
        self.ui.ui_pages.btn_data_escolhida.clicked.connect(self.data_escolhida)

        # opcao de data caixa a fechar
        self.ui.ui_pages.opcao_cx_a_fechar.toggled.connect(self.opcao_caixa_a_fechar)

        # opcao de data caixa fechado
        self.ui.ui_pages.opcao_cx_fechado.toggled.connect(self.opcao_caixa_fechado)

        # opcao de data caixa outros
        self.ui.ui_pages.opcao_cx_outros.toggled.connect(self.opcao_caixa_outros)

        # tabela despesas caixa sinal de conexao
        #self.ui.ui_pages.table_ver_despesas.selectionModel().selectionChanged.connect(self.celula_selecionada_despesas_caixa)

        # deletar despesa de caixa
        self.ui.ui_pages.btn_deletar_despesa_cx.clicked.connect(self.deletar_despesa_caixa)

        # contagem_troco
        self.ui.ui_pages.input_moedas_005.textEdited.connect(self.contagem_troco_moedas)
        self.ui.ui_pages.input_moedas_010.textEdited.connect(self.contagem_troco_moedas)
        self.ui.ui_pages.input_moedas_025.textEdited.connect(self.contagem_troco_moedas)
        self.ui.ui_pages.input_moedas_050.textEdited.connect(self.contagem_troco_moedas)                                                              
        self.ui.ui_pages.input_moedas_100.textEdited.connect(self.contagem_troco_moedas)

        self.ui.ui_pages.input_notas_2.textEdited.connect(self.contagem_troco_dinheiro)
        self.ui.ui_pages.input_notas_5.textEdited.connect(self.contagem_troco_dinheiro)
        self.ui.ui_pages.input_notas_10.textEdited.connect(self.contagem_troco_dinheiro)
        self.ui.ui_pages.input_notas_20.textEdited.connect(self.contagem_troco_dinheiro)
        self.ui.ui_pages.input_notas_50.textEdited.connect(self.contagem_troco_dinheiro)
        self.ui.ui_pages.input_notas_100.textEdited.connect(self.contagem_troco_dinheiro)
        self.ui.ui_pages.input_notas_200.textEdited.connect(self.contagem_troco_dinheiro)

        # botao atualizar leitura vendas do arquivo excel
        self.ui.ui_pages.btn_atualizar_vendas.clicked.connect(self.atualizar_vendas_arquivo)

        # botao adicionar_despesa_clicado
        self.ui.ui_pages.btn_enviar_despesa_caixa.clicked.connect(self.enviar_despesa_caixa)

        # inserindo itens ao Combo Box Trocas e Devolucoes
        self.ui.ui_pages.combo_entrada_troca_dev.addItem('---Selecione---')
        self.ui.ui_pages.combo_entrada_troca_dev.setItemData(0, '0')
        self.ui.ui_pages.combo_entrada_troca_dev.addItem('Produto')
        self.ui.ui_pages.combo_entrada_troca_dev.setItemData(1, '1')
        self.ui.ui_pages.combo_entrada_troca_dev.addItem('Dinheiro')
        self.ui.ui_pages.combo_entrada_troca_dev.setItemData(2, '2')
        self.ui.ui_pages.combo_entrada_troca_dev.addItem('Débito')
        self.ui.ui_pages.combo_entrada_troca_dev.setItemData(3, '3')
        self.ui.ui_pages.combo_entrada_troca_dev.addItem('Crédito') 
        self.ui.ui_pages.combo_entrada_troca_dev.setItemData(4, '4')       
        
        self.ui.ui_pages.combo_saida_troca_dev.addItem('---Selecione---')
        self.ui.ui_pages.combo_saida_troca_dev.setItemData(0, '0')
        self.ui.ui_pages.combo_saida_troca_dev.addItem('Produto')
        self.ui.ui_pages.combo_saida_troca_dev.setItemData(1, '1')
        self.ui.ui_pages.combo_saida_troca_dev.addItem('Dinheiro')
        self.ui.ui_pages.combo_saida_troca_dev.setItemData(2, '2')
        self.ui.ui_pages.combo_saida_troca_dev.addItem('Débito')
        self.ui.ui_pages.combo_saida_troca_dev.setItemData(3, '3')
        self.ui.ui_pages.combo_saida_troca_dev.addItem('Crédito')
        self.ui.ui_pages.combo_saida_troca_dev.setItemData(4, '4')

        # apurar resultado do caixa
        self.ui.ui_pages.btn_apurar_resultado_caixa.clicked.connect(self.apuracao_resultado_caixa)

        # enviar fechamento do caixa para bd
        self.ui.ui_pages.btn_enviar_fechamento_caixa.clicked.connect(self.enviar_fechamento_caixa)

        # caixa visto
        self.ui.ui_pages.btn_caixa_visto.clicked.connect(self.caixa_visto)

        # FECHAMENTO parcial
        self.ui.ui_pages.btn_enviar_fechamento_parcial_caixa.clicked.connect(self.enviar_fechamento_parcial_caixa)

        # INSERIR observacao no caixa
        self.ui.ui_pages.btn_inserir_observacao.clicked.connect(self.inserir_observacao)

        # DELETAR observacao no caixa
        self.ui.ui_pages.btn_deletar_observacao.clicked.connect(self.deletar_observacao)

        # INSERIR entrada trocas devolucoes no caixa
        self.ui.ui_pages.btn_inserir_entrada_troca_dev.clicked.connect(self.inserir_entrada_troca_dev)

        # INSERIR entrada trocas devolucoes no caixa
        self.ui.ui_pages.btn_inserir_saida_troca_dev.clicked.connect(self.inserir_saida_troca_dev)

        # DELETAR troca devolucao no caixa
        self.ui.ui_pages.btn_deletar_id_troca_devol.clicked.connect(self.deletar_troca_dev)

        # limpar campos facilitador troco de caixa
        self.ui.ui_pages.btn_limpar_campos_facilitador_troco_cx.clicked.connect(self.limpar_campos_facilitador_troco_cx)

        # define a data de fechamento de caixa
        self.opcao_caixa_a_fechar()

        # btn enviar facilitador troco para fechamento caixa
        self.ui.ui_pages.btn_enviando_facilitador_troco_para_fechamento_caixa.clicked.connect(self.enviando_facilitador_troco_para_fechamento_caixa)

        # inserir entradas n operadora
        self.ui.ui_pages.btn_inserir_entradas_n_operadora.clicked.connect(self.inserir_entradas_n_operadora)

        # deletar entradas n operadora
        self.ui.ui_pages.btn_deletar_entradas_n_operadora.clicked.connect(self.deletar_entradas_n_operadora)

        self.combo_box_entradas_n_operadora()
        self.combo_box_despesas_caixa()

        self.ui.ui_pages.input_troco_fecham_cx.textChanged.connect(self.apuracao_resultado_caixa)
        self.ui.ui_pages.input_estoque_troco_fecham_cx.textChanged.connect(self.apuracao_resultado_caixa)
        self.ui.ui_pages.input_total_maq_cartoes_fecham_cx.textChanged.connect(self.apuracao_resultado_caixa)

        # tabela trocas e devolucoes
        self.ui.ui_pages.tableView_troca_devolucoes_cx.clicked.connect(self.table_trocas_dev_clicada)

        # tabela observacoes
        self.ui.ui_pages.tableView_observacoes_cx.clicked.connect(self.table_observacoes_cx_clicada)

        # tabela entradas n operadora
        self.ui.ui_pages.tableView_entradas_n_operadora.clicked.connect(self.table_entradas_n_operadora_clicada)

        # tabela ver despesas
        self.ui.ui_pages.table_ver_despesas.clicked.connect(self.table_ver_despesas_clicada)

        # dia loja fechada confirmacao
        self.ui.ui_pages.checkBox_loja_fechada.clicked.connect(self.confirmacao_dia_loja_fechada)

        # EXIBIR A TELA
        self.show()

    def atualizar_vendas_arquivo(self):
        #print(self.data_selecionada_sql)
        from app.motores.leitura_arquivo_vendas import Leitura_Arquivo_Vendas
        vendas_dia = Leitura_Arquivo_Vendas(self.data_selecionada_sql).return_total_sales_day()
        valor_str = valor_float_be_para_fe(vendas_dia)
        self.ui.ui_pages.vendas_lida_dia_fecham_cx.setText(valor_str)
        self.apuracao_resultado_caixa()

    def ver_fechamentos_parciais_cx(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_fechamentos_parciais_cx)
        self.ui.top_bar_right_label.setText("| Fechamentos Parciais de Caixa")

    def confirmacao_dia_loja_fechada(self):

        if self.ui.ui_pages.checkBox_loja_fechada.isChecked() == False:
            return
        
        resposta = self.show_message_answer('Confirmação','Realmente quer que o caixa fique todo zerado?\nSerá tratado como dia com a loja fechada. Confirma?')

        if resposta == False:
            self.ui.ui_pages.checkBox_loja_fechada.setChecked(False)
    
    def table_trocas_dev_clicada(self, index):
        """Slot para processar cliques na tabela."""
        row = index.row()  # Linha clicada
        coluna = index.column()
        modelo = self.ui.ui_pages.tableView_troca_devolucoes_cx.model()
        first_col_index = index.sibling(row, 0)  # Índice da primeira coluna (coluna 0)
        valor = modelo.data(first_col_index, Qt.DisplayRole)  # Valor da célula
        self.ui.ui_pages.input_id_deletar_troca_devol.setText(str(valor))

    def table_entradas_n_operadora_clicada(self, index):
        pass
        # tableView_entradas_n_operadora
        # input_id_deletar_entradas_n_operadora
        """Slot para processar cliques na tabela."""
        row = index.row()  # Linha clicada
        coluna = index.column()
        modelo = self.ui.ui_pages.tableView_entradas_n_operadora.model()
        first_col_index = index.sibling(row, 0)  # Índice da primeira coluna (coluna 0)
        valor = modelo.data(first_col_index, Qt.DisplayRole)  # Valor da célula
        self.ui.ui_pages.input_id_deletar_entradas_n_operadora.setText(str(valor))

    def table_ver_despesas_clicada(self, index):        
        # table_ver_despesas
        # input_id_despesa_caixa_a_deletar
        """Slot para processar cliques na tabela."""
        row = index.row()  # Linha clicada
        coluna = index.column()
        modelo = self.ui.ui_pages.table_ver_despesas.model()
        first_col_index = index.sibling(row, 0)  # Índice da primeira coluna (coluna 0)
        valor = modelo.data(first_col_index, Qt.DisplayRole)  # Valor da célula
        self.ui.ui_pages.input_id_despesa_caixa_a_deletar.setText(str(valor))

    def table_observacoes_cx_clicada(self, index):
        # input_id_observacao_a_deletar
        row = index.row()  # Linha clicada
        coluna = index.column()
        modelo = self.ui.ui_pages.tableView_observacoes_cx.model()
        first_col_index = index.sibling(row, 0)  # Índice da primeira coluna (coluna 0)
        valor = modelo.data(first_col_index, Qt.DisplayRole)  # Valor da célula
        self.ui.ui_pages.input_id_observacao_a_deletar.setText(str(valor))

    def repetir_troco_cx(self):
        self.ui.ui_pages.input_troco_fecham_cx.setText(self.ui.ui_pages.input_troco_fecham_cx_anterior.text())        
        self.apuracao_resultado_caixa()

    def repetir_estoque_troco_cx(self):
        self.ui.ui_pages.input_estoque_troco_fecham_cx.setText(self.ui.ui_pages.input_est_troco_fecham_cx_ant.text())
        self.apuracao_resultado_caixa()

    def initial_page(self):
        texto = f"Usuário(a) {self.name_user} no dia {self.data_br} está no modo {self.modo}.\nSignificado do modo: {self.significacao_modo}."
        self.ui.ui_pages.textBrowser_initial_page.setText(texto)

        self.ui.pages.setCurrentWidget(self.ui.ui_pages.initial_page)
        self.ui.top_bar_right_label.setText("| Página Inicial pós login")        

    def inserir_entrada_troca_dev(self):
        from app.utilitarios.utilitarios import inserir_troca_devolucao
        
        input_descricao_entrada_troca_devol = self.ui.ui_pages.input_descricao_entrada_troca_devol.text()
        input_valor_entrada_troca_devol = valor_str_fe_para_be(self.ui.ui_pages.input_valor_entrada_troca_devol.text())
        combo_entrada_troca_dev = self.ui.ui_pages.combo_entrada_troca_dev.currentData()
        relevancia = self.ui.ui_pages.checkBox_relevancia_entrada_cx.isChecked()
        
        if relevancia == True:
            relevancia_sql = 1
        
        if relevancia == False:
            relevancia_sql = 0

        inserir_troca_devolucao(self.caixa_id, input_descricao_entrada_troca_devol, combo_entrada_troca_dev, input_valor_entrada_troca_devol, 'E', relevancia_sql, self.code_user)
        self.busca_trocas_devolucoes_caixa()
        self.fc_limpa_trocas_dev_caixa()

    def inserir_saida_troca_dev(self):
        from app.utilitarios.utilitarios import inserir_troca_devolucao

        input_descricao_saida_troca_devol = self.ui.ui_pages.input_descricao_saida_troca_devol.text()
        input_valor_saida_troca_devol = valor_str_fe_para_be(self.ui.ui_pages.input_valor_saida_troca_devol.text())
        combo_saida_troca_dev = self.ui.ui_pages.combo_saida_troca_dev.currentData()

        relevancia = self.ui.ui_pages.checkBox_relevancia_saida_cx.isChecked()
        
        if relevancia == True:
            relevancia_sql = 1
        
        if relevancia == False:
            relevancia_sql = 0

        inserir_troca_devolucao(self.caixa_id, input_descricao_saida_troca_devol, combo_saida_troca_dev, input_valor_saida_troca_devol, 'S', relevancia_sql, self.code_user)
        self.busca_trocas_devolucoes_caixa()
        self.fc_limpa_trocas_dev_caixa()

    def fc_limpa_trocas_dev_caixa(self):
        self.ui.ui_pages.input_descricao_entrada_troca_devol.clear()
        self.ui.ui_pages.input_valor_entrada_troca_devol.clear()
        self.ui.ui_pages.combo_entrada_troca_dev.setCurrentIndex(0)
        self.ui.ui_pages.input_descricao_saida_troca_devol.clear()
        self.ui.ui_pages.input_valor_saida_troca_devol.clear()
        self.ui.ui_pages.combo_saida_troca_dev.setCurrentIndex(0)
        self.ui.ui_pages.input_id_deletar_troca_devol.setText('')

    def deletar_troca_dev(self):
        from app.utilitarios.utilitarios import deletar_troca_devolucao_caixa
        id_troca_dev = int(valor_str_fe_para_be(self.ui.ui_pages.input_id_deletar_troca_devol.text()))

        resposta = self.show_message_answer('Confimação',f'Realmente quer deletar a troca/devol de ID: {id_troca_dev} ?')

        if resposta == False:            
            self.ui.ui_pages.input_id_deletar_troca_devol.setText('')
            self.show_message_info('Info','Nada será deletado.')
            return

        delecao = deletar_troca_devolucao_caixa(id_troca_dev)

        if delecao == False:
            self.show_message_warning('ERRO','Algo deu errado na deleção na tabela de Trocas e Devoluções.')

        self.ui.ui_pages.input_id_deletar_troca_devol.clear()
        self.busca_trocas_devolucoes_caixa()
        self.fc_limpa_trocas_dev_caixa()
        self.apuracao_resultado_caixa()

    def inserir_observacao(self):
        from app.utilitarios.utilitarios import inserir_observacao_caixa
        textBrowser_observacao_cx = self.ui.ui_pages.textEdit_observacao_cx.toPlainText()

        if len(textBrowser_observacao_cx) == 0:
            self.show_message_info('Em branco','Observação necessita ser inserida, esá em branco.')
            return
        
        insercao = inserir_observacao_caixa(textBrowser_observacao_cx, self.caixa_id, usuario_id = self.code_user)
        self.show_message_info('Inserção da Observação',f'Resultado da Inserção da Observação: {insercao}')        
        self.ui.ui_pages.textEdit_observacao_cx.clear()
        self.busca_observacoes_caixa()

    def deletar_observacao(self):
        from app.utilitarios.utilitarios import deletar_observacao_caixa
        input_id_observacao_a_deletar = int(valor_str_fe_para_be(self.ui.ui_pages.input_id_observacao_a_deletar.text()))

        resposta = self.show_message_answer('Confimação',f'Realmente quer deletar a observação de ID: {input_id_observacao_a_deletar} ?')

        if resposta == False:            
            self.ui.ui_pages.self.ui.ui_pages.input_id_observacao_a_deletar.setText('')
            self.show_message_info('Info','Nada será deletado.')
            return

        deletar_observacao_caixa(input_id_observacao_a_deletar)
        self.ui.ui_pages.input_id_observacao_a_deletar.clear()
        self.busca_observacoes_caixa()

    def caixa_visto(self):
        self.escolha_data_cx_button()

    def enviar_fechamento_parcial_caixa(self):
        from app.utilitarios.utilitarios import inserir_fechamento_caixa_parcial

        valor_vendas_dia = valor_str_fe_para_be(self.ui.ui_pages.vendas_lida_dia_fecham_cx.text())        

        if valor_vendas_dia == 0:

            resposta = self.show_message_answer('Confirmação','Fechar parcialmente o caixa sem nada vendido?')

            if resposta == False:
                return

            if resposta == True:
                self.ui.ui_pages.vendas_lida_dia_fecham_cx.setText('0,00')

        if self.ui.ui_pages.input_total_maq_cartoes_fecham_cx.text() == '':
            self.show_message_warning('ERRO','Necessita preencher o campo de vendas da Máquina de Cartões.')
            return
                
        vendas_maquina = valor_str_fe_para_be(self.ui.ui_pages.input_total_maq_cartoes_fecham_cx.text())

        if vendas_maquina == 0:

            resposta = self.show_message_answer('Confirmação','Nada foi vendido nas máquinas?')

            if resposta == False:
                return

            if resposta == True:
                self.ui.ui_pages.input_total_maq_cartoes_fecham_cx.setText('0,00')
        
        if self.ui.ui_pages.input_troco_fecham_cx.text() == '':
            self.show_message_warning('Em branco','Troco de caixa em branco. Prencher.')
            return

        if self.ui.ui_pages.input_estoque_troco_fecham_cx.text() == '':
            self.show_message_warning('Em branco','Estoque de troco de caixa em branco. Prencher.')
            return

        self.apuracao_resultado_caixa()

        resultado_final_cx = valor_str_fe_para_be(self.ui.ui_pages.input_resultado_fecham_cx.text())
        troco_final_cx = valor_str_fe_para_be(self.ui.ui_pages.input_troco_fecham_cx.text())
        estoque_troco_final_cx = valor_str_fe_para_be(self.ui.ui_pages.input_estoque_troco_fecham_cx.text())
        vendas_dinheiro_dia = valor_str_fe_para_be(self.ui.ui_pages.input_vendas_dinheiro_dia_fecham_cx.text())
        vendas_pix_direto_cpf = valor_str_fe_para_be(self.ui.ui_pages.input_vendas_pix_direto_cpf_dia_fecham_cx.text())
        vendas_pix_direto_cnpj = valor_str_fe_para_be(self.ui.ui_pages.input_vendas_pix_direto_cnpj_dia_fecham_cx.text())
        trocas_dev_produtos = valor_str_fe_para_be(self.ui.ui_pages.input_trocas_devolucoes_produtos.text())
        trocas_dev_dinheiro = valor_str_fe_para_be(self.ui.ui_pages.input_trocas_devolucoes_dinheiro.text())
        trocas_dev_debito = valor_str_fe_para_be(self.ui.ui_pages.input_trocas_devolucoes_debito.text())
        trocas_dev_credito = valor_str_fe_para_be(self.ui.ui_pages.input_trocas_devolucoes_credito.text())

        texto_confirmacao = f'''resultado_final_cx: {resultado_final_cx}\n\n
        vendas: {valor_vendas_dia}\n\n
        valor vendas máquina: {vendas_maquina}\n\n
        troco_final_cx: {troco_final_cx}\n
        estoque_troco_final_cx: {estoque_troco_final_cx}\n
        vendas_dinheiro_dia: {vendas_dinheiro_dia}\n
        vendas_pix_direto_cpf: {vendas_pix_direto_cpf}\n
        vendas_pix_direto_cnpj: {vendas_pix_direto_cnpj}\n
        trocas_dev_produtos: {trocas_dev_produtos}\n
        trocas_dev_dinheiro: {trocas_dev_dinheiro}\n
        trocas_dev_debito: {trocas_dev_debito}\n 
        trocas_dev_credito: {trocas_dev_credito}\n
        '''

        resposta_2 = self.show_message_answer('Confirmação',f'Deseja fechar o caixa parcialmente com os seguintes dados:\n{texto_confirmacao}')

        if resposta_2 == False:
            return

        insercao = inserir_fechamento_caixa_parcial(self.caixa_id, self.code_user, resultado_final_cx, troco_final_cx, estoque_troco_final_cx, valor_vendas_dia, vendas_dinheiro_dia, vendas_pix_direto_cpf, vendas_pix_direto_cnpj, vendas_maquina, trocas_dev_dinheiro, trocas_dev_debito, trocas_dev_credito, trocas_dev_produtos)

        if insercao == True:
            self.show_message_info('OK','Inserção de Caixa Parcial feita. OK')
            self.escolha_data_cx_button()

        if insercao == False:
            self.show_message_warning('ERRO','Inserção de Caixa Parcial não foi feita. Problema')
            

    def enviar_fechamento_caixa(self):
        from app.utilitarios.utilitarios import inserir_fechamento_caixa_definitivo
        self.apuracao_resultado_caixa()
        self.validacao_fechamento_caixa_definitivo()

        if self.validador_fechamento_caixa_definitivo:

            if self.dia_loja_fechada == False:
                insercao_ok = inserir_fechamento_caixa_definitivo(self.data_selecionada_sql, self.caixa_id, self.code_user, self.resultado_final_caixa, self.troco_cx, self.estoque_troco_cx, self.vendas_dia_total, self.vendas_dinheiro, self.vendas_pix_direto_cnpj, self.vendas_pix_direto_cpf, self.tot_maq_cartoes, self.valor_troca_dev_dinheiro, self.valor_troca_dev_debito, self.valor_troca_dev_credito, self.valor_troca_dev_produtos, 0)

            if self.dia_loja_fechada == True:
                insercao_ok = inserir_fechamento_caixa_definitivo(self.data_selecionada_sql, self.caixa_id, self.code_user, self.resultado_final_caixa, self.troco_cx, self.estoque_troco_cx, self.vendas_dia_total, self.vendas_dinheiro, self.vendas_pix_direto_cnpj, self.vendas_pix_direto_cpf, self.tot_maq_cartoes, self.valor_troca_dev_dinheiro, self.valor_troca_dev_debito, self.valor_troca_dev_credito, self.valor_troca_dev_produtos, 1)

            if insercao_ok == True:
                self.show_message_info("Inserido.","Fechamento de Caixa Inserido.")
                
                if self.modo != 'fechado':
                    self.vendas_dia_obj.save_datas_sales()

                self.escolha_data_cx_button()
                self.ui.ui_pages.opcao_cx_fechado.setChecked(True)
                self.ui.ui_pages.checkBox_loja_fechada.setChecked(False)

    def validacao_fechamento_caixa_definitivo(self):

        self.validador_fechamento_caixa_definitivo = False

        if self.ui.ui_pages.input_total_maq_cartoes_fecham_cx.text() == '':
            self.show_message_warning('Total dos Cartões','Total das vendas na máquina necessita ser preenchido.')
            return

        if self.ui.ui_pages.input_troco_fecham_cx.text() == '':
            self.show_message_warning('Troco','Troco de caixa necessita ser preenchido.')
            return

        if self.ui.ui_pages.input_estoque_troco_fecham_cx.text() == '':
            self.show_message_warning('Estoque de Troco','Estoque de Troco de caixa necessita ser preenchido.')
            return

        soma_entradas = (self.vendas_dinheiro + self.vendas_pix_direto_cnpj + self.vendas_pix_direto_cpf + self.tot_maq_cartoes)

        diferenca = self.vendas_dia_total - soma_entradas

        if diferenca <= 0.01 and diferenca >= -0.01:
            self.validador_fechamento_caixa_definitivo = True
        else:
            self.show_message_info('Diferença',"Soma das entradas não bate com as vendas do Dia.")

        resposta = self.show_message_answer('Fechamento de Caixa',f'O resultado final do caixa é de {self.ui.ui_pages.input_resultado_fecham_cx.text()}.\nProssegue com o fechamento?')

        if resposta == QMessageBox.StandardButton.No:
            return False

        if resposta == QMessageBox.StandardButton.Yes:
            return True

    def apuracao_resultado_caixa(self):

        try:
            self.vendas_dia_total = valor_str_fe_para_be(self.ui.ui_pages.vendas_lida_dia_fecham_cx.text())
        except:
            self.show_message_info("Vendas do total do dia","Vendas total do dia precisa ser informada.")

        try:
            self.tot_maq_cartoes = valor_str_fe_para_be(self.ui.ui_pages.input_total_maq_cartoes_fecham_cx.text())
        except:
            self.show_message_info("Máquina de Cartões","Valor maq de cartões precisa ser informado.")

        try:
            self.vendas_pix_direto_cnpj = valor_str_fe_para_be(self.ui.ui_pages.input_vendas_pix_direto_cnpj_dia_fecham_cx.text())
        except:
            self.show_message_info("PIX direto CNPJ","Valor PIX direto CNPJ precisa ser informado.")

        try:
            self.vendas_pix_direto_cpf = valor_str_fe_para_be(self.ui.ui_pages.input_vendas_pix_direto_cpf_dia_fecham_cx.text())
        except:
            self.show_message_info("PIX direto CPF","Valor PIX direto CPF precisa ser informado.")

        try:
            self.vendas_dinheiro = valor_str_fe_para_be(self.ui.ui_pages.input_vendas_dinheiro_dia_fecham_cx.text())
        except:
            self.show_message_info("Vendas Dinheiro","Vendas em Dinheiro precisa ser informado.")
        
        try:
            self.despesas = valor_str_fe_para_be(self.ui.ui_pages.input_total_despesas_caixa_fecham_cx.text())
        except:
            self.show_message_info("Despesas","Despesas precisa ser informada.")

        try:
            self.valor_troca_dev_produtos = valor_str_fe_para_be(self.ui.ui_pages.input_trocas_devolucoes_produtos.text())
        except:
            self.show_message_info("Trocas/Devoluções","Valor de Trocas/Devoluções Produtos precisa ser preenchido.")

        try:
            self.valor_troca_dev_dinheiro = valor_str_fe_para_be(self.ui.ui_pages.input_trocas_devolucoes_dinheiro.text())
        except:
            self.show_message_info("Trocas/Devoluções","Valor de Trocas/Devoluções Dinheiro precisa ser preenchido.")

        try:
            self.valor_troca_dev_debito = valor_str_fe_para_be(self.ui.ui_pages.input_trocas_devolucoes_debito.text())
        except:
            self.show_message_info("Trocas/Devoluções","Valor de Trocas/Devoluções Débito precisa ser preenchido.")

        try:
            self.valor_troca_dev_credito = valor_str_fe_para_be(self.ui.ui_pages.input_trocas_devolucoes_credito.text())
        except:
            self.show_message_info("Trocas/Devoluções","Valor de Trocas/Devoluções Crédito precisa ser preenchido.")     

        try:
            self.troco_cx = valor_str_fe_para_be(self.ui.ui_pages.input_troco_fecham_cx.text())
        except:
            self.show_message_info("Troco de caixa", "Troco de caixa precisa ser preenchido.")
        
        try:
            self.estoque_troco_cx = valor_str_fe_para_be(self.ui.ui_pages.input_estoque_troco_fecham_cx.text())
        except:
            self.show_message_info("Estoque Troco de Cx", "estoque de troco de Caixa precisa ser preenchido.")
        
        try:
            self.troco_cx_anterior = valor_str_fe_para_be(self.ui.ui_pages.input_troco_fecham_cx_anterior.text())
        except:
            self.show_message_info("Troco de Caixa Anterior", "troco de cx necessita ser preenchido.")

        try:
            self.estoque_troco_cx_anterior = valor_str_fe_para_be(self.ui.ui_pages.input_est_troco_fecham_cx_ant.text())
        except:
            self.show_message_info("Estoque Troco de Caixa Anterior", "Valor do estoque de troco anterior tem que ser preenchido.")

        if self.modo == 'completo' and valor_str_fe_para_be(self.ui.ui_pages.input_total_maq_cartoes_fecham_cx.text()) > valor_str_fe_para_be(self.ui.ui_pages.vendas_lida_dia_fecham_cx.text()):
            self.show_message_warning('Problema','Valor das entradas na máquina maior que o das vendas. Verificar!!')            
        
        self.resultado_troco_caixa = self.troco_cx + self.estoque_troco_cx - self.troco_cx_anterior - self.estoque_troco_cx_anterior
        self.ui.ui_pages.result_troco_fechamento_cx.setText(valor_float_be_para_fe(self.resultado_troco_caixa))

        self.entradas_caixa = self.tot_maq_cartoes + self.vendas_pix_direto_cnpj + self.vendas_pix_direto_cpf - self.valor_troca_dev_credito - self.valor_troca_dev_debito - self.valor_troca_dev_dinheiro + self.resultado_troco_caixa
        self.saidas_caixa = self.vendas_dia_total - self.despesas
        
        self.resultado_final_caixa = - self.saidas_caixa + self.entradas_caixa
        self.ui.ui_pages.input_resultado_fecham_cx.setText(valor_float_be_para_fe(self.resultado_final_caixa))

        dif = (self.vendas_dia_total - (self.vendas_dinheiro + self.vendas_pix_direto_cnpj + self.vendas_pix_direto_cpf + self.tot_maq_cartoes)) * (-1)
        self.ui.ui_pages.input_diferenca.setText(valor_float_be_para_fe(round(dif,2)))

    def deletar_despesa_caixa(self):

        from app.utilitarios.utilitarios import deletar_despesa_caixa

        id_despesa_caixa = int(valor_str_fe_para_be(self.ui.ui_pages.input_id_despesa_caixa_a_deletar.text()))

        resposta = self.show_message_answer('Confirmação',f'Deseja apagar a despesa de caixa de ID: {id_despesa_caixa} ?')

        if resposta == False:
            self.ui.ui_pages.input_id_despesa_caixa_a_deletar.setText('')
            self.show_message_info('Aviso','Nada será deletado.')
            return
        
        if id_despesa_caixa != '':
            deletar_despesa_caixa(id_despesa_caixa)

        if id_despesa_caixa == '':
            self.show_message_info("ID não preenchido","Precisa digitar o ID da despesa de Caixa para ser deletado.")
        
        self.ver_despesas_cx_button()

    def enviar_despesa_caixa(self):

        from app.utilitarios.utilitarios import inserir_despesa_caixa, retorna_id_dados_fechamento_caixa_entra_data_sql

        index = self.ui.ui_pages.despesa_id_comboBox.currentIndex()

        if index == 0:
            self.show_message_warning("Selecionar","Precisa selecionar o tipo da despesa")

        if index >= 0:
            item_id = self.ui.ui_pages.despesa_id_comboBox.itemData(index)
            texto = self.ui.ui_pages.despesa_id_comboBox.currentText()

        valor_despesa = self.ui.ui_pages.valor_despesa_input.text()
        valor_despesa = valor_despesa.replace(',','.')

        try:
            valor_despesa = float(valor_despesa)
        except:
            self.show_message_warning("Valor","Valor da despesa está irregular.")
            return

        descricao_despesa = self.ui.ui_pages.descricao_despesa_input.toPlainText()
        
        inserir = inserir_despesa_caixa(descricao_despesa=(descricao_despesa + ' - ' + texto), valor_despesa=valor_despesa, despesa_id=item_id, caixa_id=self.caixa_id, usuario_id=self.code_user)

        if inserir == False:
            self.show_message_warning("ERRO","Algo deu errado com a inserção da Despesa.")

        if inserir:
            self.show_message_info("Inserido","Despesa inserida.")
        
        self.cria_lista_despesas_caixa()
        self.busca_despesas_caixa()
        self.apuracao_resultado_caixa()    
        self.limpar_campos_despesa_caixa()

    def limpar_campos_despesa_caixa(self):
        self.ui.ui_pages.descricao_despesa_input.setText('')
        self.ui.ui_pages.valor_despesa_input.setText('')
        self.ui.ui_pages.input_id_despesa_caixa_a_deletar.setText('')

    def data_escolhida(self):
        
        self.data_atual()

        from app.motores.leitura_arquivo_vendas import Leitura_Arquivo_Vendas
        from app.utilitarios.utilitarios import retorna_id_dados_fechamento_caixa_entra_data_sql     

        if self.ui.ui_pages.opcao_cx_a_fechar.isChecked() or self.ui.ui_pages.opcao_cx_fechado.isChecked() or self.ui.ui_pages.opcao_cx_outros.isChecked():
            pass
        else:
            self.show_message_warning("Precisa selecionar...", "Precisa selecionar o tipo de caixa que quer.")
            return

        self.data_selecionada_qdate = self.ui.ui_pages.calendario_widget.selectedDate()
        self.data_selecionada_sql = self.data_selecionada_qdate.toString("yyyy-MM-dd")

        self.data_br = self.data_selecionada_qdate.toString("dd-MM-yyyy")

        self.caixa_id = retorna_id_dados_fechamento_caixa_entra_data_sql(self.data_selecionada_sql)

        self.choiced_date = True

        self.ui.ui_pages.data_cx_fechamento_cx.setDate(self.data_selecionada_qdate)
        self.ui.ui_pages.data_cx_ver_despesa.setDate(self.data_selecionada_qdate)
        self.ui.ui_pages.data_cx_observacao.setDate(self.data_selecionada_qdate)        
        self.ui.ui_pages.data_inserir_despesa.setDate(self.data_selecionada_qdate)
        self.ui.ui_pages.data_cx_trocas_devolucoes.setDate(self.data_selecionada_qdate)
        self.ui.ui_pages.data_cx_entradas_n_operadora.setDate(self.data_selecionada_qdate)

        self.ui.ui_pages.data_cx_fechamento_cx.setReadOnly(True)
        self.ui.ui_pages.data_cx_ver_despesa.setReadOnly(True)
        self.ui.ui_pages.data_cx_observacao.setReadOnly(True)
        self.ui.ui_pages.data_inserir_despesa.setReadOnly(True)
        self.ui.ui_pages.data_cx_trocas_devolucoes.setReadOnly(True)
        self.ui.ui_pages.data_cx_entradas_n_operadora.setReadOnly(True)

        self.vendas_dia_obj = Leitura_Arquivo_Vendas(self.data_selecionada_sql)
        self.exist_file_sales = self.vendas_dia_obj.return_exist_file()

        self.dia_loja_fechada = self.ui.ui_pages.checkBox_loja_fechada.isChecked()

        if self.dia_loja_fechada and self.exist_file_sales:
            self.show_message_warning('ERRO',"Vendas existem, tem-se o arquivo de vendas.")
        
        self.busca_troco_anterior()
        self.define_modo()
        self.busca_despesas_caixa()
        self.busca_observacoes_caixa()
        self.busca_trocas_devolucoes_caixa()
        self.busca_entradas_n_operadora()
        self.busca_fechamentos_parciais_caixa()

        if self.dia_loja_fechada == True:
            resposta = self.show_message_answer('Loja Fechada','Setar como loja fechada neste dia. Não houve vendas?')

            if self.exist_file_sales == False and self.ui.ui_pages.opcao_cx_a_fechar.isChecked() and resposta == True:
                self.fc_dia_loja_fechada()

        # INITIAL PAGE
        self.initial_page()

    def busca_fechamentos_parciais_caixa(self):
        from app.utilitarios.utilitarios import return_dict_fechamentos_parciais_cx
        lista_fecham_parciais = return_dict_fechamentos_parciais_cx(self.caixa_id)

        if lista_fecham_parciais == 0:
            self.ui.ui_pages.label_fecham_parc_cx.setText('Não há fecham parciais.')
            return

        self.ui.ui_pages.label_fecham_parc_cx.setText('Há fecham parciais.')
        self.tabela_fechamentos_parciais(lista_fecham_parciais)

    def fc_dia_loja_fechada(self):
        self.ui.ui_pages.input_troco_fecham_cx.setText(self.ui.ui_pages.input_troco_fecham_cx_anterior.text())
        self.ui.ui_pages.input_estoque_troco_fecham_cx.setText(self.ui.ui_pages.input_est_troco_fecham_cx_ant.text())
        self.ui.ui_pages.vendas_lida_dia_fecham_cx.setText('0,00')
        self.ui.ui_pages.input_resultado_fecham_cx.setText('0,00')
        self.ui.ui_pages.input_total_maq_cartoes_fecham_cx.setText('0,00')
        self.ui.ui_pages.input_vendas_dinheiro_dia_fecham_cx.setText('0,00')
        self.ui.ui_pages.input_vendas_pix_direto_cnpj_dia_fecham_cx.setText('0,00')
        self.ui.ui_pages.input_vendas_pix_direto_cpf_dia_fecham_cx.setText('0,00')
        self.ui.ui_pages.input_diferenca.setText('0,00')
        self.apuracao_resultado_caixa()
        self.enviar_fechamento_caixa()

    def limpa_dados_fechamento_caixa(self):
        self.ui.ui_pages.input_total_maq_cartoes_fecham_cx.clear()
        self.ui.ui_pages.input_vendas_dinheiro_dia_fecham_cx.clear()
        self.ui.ui_pages.input_vendas_pix_direto_cnpj_dia_fecham_cx.clear()
        self.ui.ui_pages.input_vendas_pix_direto_cpf_dia_fecham_cx.clear()
        self.ui.ui_pages.input_troco_fecham_cx.clear()
        self.ui.ui_pages.input_estoque_troco_fecham_cx.clear()
        self.ui.ui_pages.result_troco_fechamento_cx.clear()
        self.ui.ui_pages.input_total_despesas_caixa_fecham_cx.clear()
        self.ui.ui_pages.vendas_lida_dia_fecham_cx.clear()
        self.ui.ui_pages.tableView_fecham_parciais.reset()
        self.ui.ui_pages.input_trocas_devolucoes_credito.clear()
        self.ui.ui_pages.input_trocas_devolucoes_debito.clear()
        self.ui.ui_pages.input_trocas_devolucoes_dinheiro.clear()
        self.ui.ui_pages.input_trocas_devolucoes_produtos.clear()
        self.ui.ui_pages.input_resultado_fecham_cx.clear()
        self.ui.ui_pages.input_diferenca.clear()

    def busca_observacoes_caixa(self):
        from app.utilitarios.utilitarios import retorna_lista_dict_observacoes_caixa_pelo_caixa_id

        dados = retorna_lista_dict_observacoes_caixa_pelo_caixa_id(self.caixa_id)

        n_linhas = len(dados)

        if n_linhas >= 1:
            self.ui.ui_pages.label_observacoes.setText('Existem.')

        if n_linhas == 0:
            self.ui.ui_pages.label_observacoes.setText('Não há.')

        model_table_observacoes = QStandardItemModel(n_linhas,2)
        model_table_observacoes.setHorizontalHeaderLabels(['ID','Observação'])

        for row, linha_dados in enumerate(dados):            
            
            item_1 = QStandardItem(str(linha_dados['id']))
            model_table_observacoes.setItem(row, 0, item_1)
            
            item_2 = QStandardItem(linha_dados['observacao_caixa'])
            model_table_observacoes.setItem(row, 1, item_2)
        
        self.ui.ui_pages.tableView_observacoes_cx.setModel(model_table_observacoes)
        self.ui.ui_pages.tableView_observacoes_cx.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

        # textEdit_observacoes_cx

    def busca_entradas_n_operadora(self):
        from app.utilitarios.utilitarios import retorna_lista_dict_insercao_entradas_n_operadora_caixa_pelo_caixa_id        

        dados = retorna_lista_dict_insercao_entradas_n_operadora_caixa_pelo_caixa_id(self.caixa_id)

        total_entrada_dinheiro = 0 #1
        total_entrada_cnpj = 0 #2
        total_entrada_cpf = 0 #3

        for item in dados:

            if item['id_tipo_entrada'] == 1:
                total_entrada_dinheiro += item['valor']

            if item['id_tipo_entrada'] == 2:
                total_entrada_cnpj += item['valor']

            if item['id_tipo_entrada'] == 3:
                total_entrada_cpf += item['valor']

        self.ui.ui_pages.input_vendas_dinheiro_dia_fecham_cx.setText(valor_float_be_para_fe(total_entrada_dinheiro))
        self.ui.ui_pages.input_vendas_pix_direto_cpf_dia_fecham_cx.setText(valor_float_be_para_fe(total_entrada_cpf))
        self.ui.ui_pages.input_vendas_pix_direto_cnpj_dia_fecham_cx.setText(valor_float_be_para_fe(total_entrada_cnpj))

        self.table_entradas_n_operadora(dados)

    def combo_box_entradas_n_operadora(self):
        # Combo BOX Entradas n Maq Operadora
        from app.utilitarios.utilitarios import retorna_lista_tuplas_id_tipos_entradas_n_operadora
        lista_tuplas_id_tipos_entradas_n_operadora = retorna_lista_tuplas_id_tipos_entradas_n_operadora()
        
        self.ui.ui_pages.comboBox_entradas_n_operadora.addItem('---Selecione--')
        self.ui.ui_pages.comboBox_entradas_n_operadora.setItemData(0,0)

        for item in lista_tuplas_id_tipos_entradas_n_operadora:
            self.ui.ui_pages.comboBox_entradas_n_operadora.addItem(item[1])
            index = self.ui.ui_pages.comboBox_entradas_n_operadora.count() - 1
            self.ui.ui_pages.comboBox_entradas_n_operadora.setItemData(index, item[0])

    def tabela_fechamentos_parciais(self, dados):

        if dados == 0:
            return

        n_linhas = len(dados)
        model_table_fechamentos_parciais = QStandardItemModel(n_linhas, 4)
        model_table_fechamentos_parciais.setHorizontalHeaderLabels(['ID','usuario','hora','result'])

        for row, linha_dados in enumerate(dados):
            
            item_1 = QStandardItem(str(linha_dados['id']))
            model_table_fechamentos_parciais.setItem(row, 0, item_1)
            
            item_2 = QStandardItem(str(linha_dados['usuario']))
            model_table_fechamentos_parciais.setItem(row, 1, item_2)
            
            item_3 = QStandardItem(f"{str(linha_dados['hora'])}:{str(linha_dados['minutos'])}")
            model_table_fechamentos_parciais.setItem(row, 2, item_3)

            item_4 = QStandardItem(str(linha_dados['resultado_cx']))
            model_table_fechamentos_parciais.setItem(row, 3, item_4)
                
        self.ui.ui_pages.tableView_fecham_parciais.setModel(model_table_fechamentos_parciais)
        self.ui.ui_pages.tableView_fecham_parciais.horizontalHeader().resizeContentsPrecision()
        return        

    def table_entradas_n_operadora(self, dados):

        n_linhas = len(dados)
        model_table_entrada_n_operadora = QStandardItemModel(n_linhas, 3)
        model_table_entrada_n_operadora.setHorizontalHeaderLabels(['ID','Entrada','Valor'])

        for row, linha_dados in enumerate(dados):
            
            item_1 = QStandardItem(str(linha_dados['id']))
            model_table_entrada_n_operadora.setItem(row, 0, item_1)
            
            item_2 = QStandardItem(str(linha_dados['tipo_entrada']))
            model_table_entrada_n_operadora.setItem(row, 1, item_2)
            
            item_3 = QStandardItem(valor_float_be_para_fe(linha_dados['valor']))
            model_table_entrada_n_operadora.setItem(row, 2, item_3)
                
        self.ui.ui_pages.tableView_entradas_n_operadora.setModel(model_table_entrada_n_operadora)
        self.ui.ui_pages.tableView_entradas_n_operadora.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        return

    def busca_trocas_devolucoes_caixa(self):
        from app.utilitarios.utilitarios import retorna_lista_dict_trocas_devolucoes_caixa_pelo_caixa_id

        dados = retorna_lista_dict_trocas_devolucoes_caixa_pelo_caixa_id(self.caixa_id)

        total_valor_entradas_din = 0
        total_valor_saidas_din = 0

        total_valor_entradas_debito = 0
        total_valor_saidas_debito = 0

        total_valor_entradas_credito = 0
        total_valor_saidas_credito = 0

        total_valor_entradas_produtos = 0
        total_valor_saidas_produtos = 0

        for linha in dados:
            id = linha['id']
            codigo = linha['codigo_produto']
            form = linha['id_forma']
            valor = linha['valor']
            in_out = linha['entrada_saida']
            relevancia_caixa = int(linha['relevancia_caixa'])

            if in_out == 'E' and form == '1' and relevancia_caixa == 1:
                total_valor_entradas_produtos += valor

            if in_out == 'S' and form == '1' and relevancia_caixa == 1:
                total_valor_saidas_produtos += valor

            if in_out == 'E' and form == '2' and relevancia_caixa == 1:
                total_valor_entradas_din += valor

            if in_out == 'S' and form == '2' and relevancia_caixa == 1:
                total_valor_saidas_din += valor
        
            if in_out == 'E' and form == '3' and relevancia_caixa == 1:
                total_valor_entradas_debito += valor

            if in_out == 'S' and form == '3' and relevancia_caixa == 1:
                total_valor_saidas_debito += valor

            if in_out == 'E' and form == '4' and relevancia_caixa == 1:
                total_valor_entradas_credito += valor

            if in_out == 'S' and form == '4' and relevancia_caixa == 1:
                total_valor_saidas_credito += valor

        self.ui.ui_pages.input_trocas_devolucoes_produtos.setText(valor_float_be_para_fe(round(total_valor_entradas_produtos-total_valor_saidas_produtos,2)))
        self.ui.ui_pages.input_trocas_devolucoes_dinheiro.setText(valor_float_be_para_fe(round(total_valor_entradas_din-total_valor_saidas_din,2)))
        self.ui.ui_pages.input_trocas_devolucoes_debito.setText(valor_float_be_para_fe(round(total_valor_entradas_debito-total_valor_saidas_debito,2)))
        self.ui.ui_pages.input_trocas_devolucoes_credito.setText(valor_float_be_para_fe(round(total_valor_entradas_credito-total_valor_saidas_credito,2)))

        diferenca_geral = (total_valor_entradas_din - total_valor_saidas_din +  total_valor_entradas_debito - total_valor_saidas_debito + total_valor_entradas_credito - total_valor_saidas_credito + total_valor_entradas_produtos - total_valor_saidas_produtos)
        self.ui.ui_pages.input_diferenca_total_trocas_devol.setText(valor_float_be_para_fe(diferenca_geral))

        # tableView_troca_devolucoes_cx
        self.table_trocas_devolucoes_caixa(dados)

    def table_trocas_devolucoes_caixa(self, dados):
        n_linhas = len(dados)
        model_table_trocas_dev = QStandardItemModel(n_linhas,6)
        model_table_trocas_dev.setHorizontalHeaderLabels(['ID','E/S','Num Pedido','Tipo','Desc./Codigo','Valor','relev'])

        for row, linha_dados in enumerate(dados):            
            
            item_0 = QStandardItem(str(linha_dados['id']))
            model_table_trocas_dev.setItem(row, 0, item_0)

            item_1 = QStandardItem((str(linha_dados['entrada_saida'])).replace(".",","))
            model_table_trocas_dev.setItem(row, 1, item_1)

            item_3 = QStandardItem((str(linha_dados['forma'])).replace(".",","))
            model_table_trocas_dev.setItem(row, 3, item_3)

            item_4 = QStandardItem(linha_dados['codigo_produto'])
            model_table_trocas_dev.setItem(row, 4, item_4)

            item_5 = QStandardItem((str(linha_dados['valor'])).replace(".",","))
            model_table_trocas_dev.setItem(row, 5, item_5)

            item_6 = QStandardItem((str(linha_dados['relevancia_caixa'])).replace(".",","))
            model_table_trocas_dev.setItem(row, 6, item_6)
        
        self.ui.ui_pages.tableView_troca_devolucoes_cx.setModel(model_table_trocas_dev)
        self.ui.ui_pages.tableView_troca_devolucoes_cx.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

    def busca_despesas_caixa(self):
        from app.utilitarios.utilitarios import retorna_lista_dict_id_despesas_caixa_pelo_caixa_id        

        dados = retorna_lista_dict_id_despesas_caixa_pelo_caixa_id(self.caixa_id)

        valor_total_despesa = 0

        for linha in dados:
            id = linha['id']
            desc_id = linha['descricao_despesa']
            valor_despesa = linha['valor_despesa']            
            valor_total_despesa += valor_despesa

        self.ui.ui_pages.input_total_despesas_caixa_fecham_cx.setText(valor_float_be_para_fe(valor_total_despesa))

        # textEdit_despesas_cx

    def combo_box_despesas_caixa(self):
        # adicionando itens às despesas de caixa
        from app.utilitarios.utilitarios import retorna_lista_tuplas_id_despesas_caixa
        lista_tuplas_id_despesas_caixa = retorna_lista_tuplas_id_despesas_caixa()

        for item in lista_tuplas_id_despesas_caixa:
            self.ui.ui_pages.despesa_id_comboBox.addItem(item[1])
            index = self.ui.ui_pages.despesa_id_comboBox.count() - 1
            self.ui.ui_pages.despesa_id_comboBox.setItemData(index, item[0])

    def data_atual(self):
        from datetime import datetime

        agora = datetime.now().date()

        dia_agora = agora.day
        mes_agora = agora.month
        ano_agora = agora.year

        self.agora_qdate = QDate(ano_agora, mes_agora, dia_agora)

    def define_modo(self):

        # opcao
        # data_agora
        # data_escolhida
        # existe arquivo de vendas
        # dia loja fechada
        
        if self.ui.ui_pages.opcao_cx_outros.isChecked():
            self.modo = 'outros'
            self.modo_outros()
            print('modo outros')
            self.define_botoes_operantes()
            return
        
        if self.ui.ui_pages.opcao_cx_fechado.isChecked():
            self.modo = 'leitura'
            self.modo_leitura()
            print('modo leitura')
            self.define_botoes_operantes()
            return

        if self.exist_file_sales and self.ui.ui_pages.opcao_cx_a_fechar.isChecked() and self.data_selecionada_qdate <= self.agora_qdate:
            self.modo = 'completo'
            self.modo_completo()
            self.define_botoes_operantes()
            return

        if not self.exist_file_sales and self.ui.ui_pages.opcao_cx_a_fechar.isChecked() and self.agora_qdate > self.data_selecionada_qdate:
            self.show_message_info("ERRO - gravar arquivo vendas","Necessita do arquivo de vendas do sistema EURO.")
            self.modo = 'pausa'
            self.modo_pausa()
            print('modo pausa')
            self.define_botoes_operantes()
            return

        if (not self.exist_file_sales and self.data_selecionada_qdate == self.agora_qdate) or (self.exist_file_sales and self.ui.ui_pages.opcao_cx_a_fechar.isChecked() and self.data_selecionada_qdate == self.agora_qdate):
            self.modo = 'parcial'
            self.modo_parcial()
            print('modo parcial')
            self.define_botoes_operantes()
            return

        if self.dia_loja_fechada == True:
            self.modo = 'fechado'
            self.significacao_modo = 'caixa zerado pois a loja estava fechada'
            self.fc_dia_loja_fechada()
            print('modo fechado')
            self.define_botoes_operantes()
            return        
        
        return

    def define_botoes_operantes(self):

        if self.modo == 'leitura':
            self.ui.ui_pages.btn_inserir_entrada_troca_dev.setEnabled(False)
            self.ui.ui_pages.btn_inserir_saida_troca_dev.setEnabled(False)
            self.ui.ui_pages.btn_deletar_id_troca_devol.setEnabled(False)
            self.ui.ui_pages.btn_inserir_entradas_n_operadora.setEnabled(False)
            self.ui.ui_pages.btn_deletar_entradas_n_operadora.setEnabled(False)
            self.ui.ui_pages.btn_inserir_despesa_cx.setEnabled(False)
            self.ui.ui_pages.btn_deletar_despesa_cx.setEnabled(False)
            self.ui.ui_pages.btn_enviar_despesa_caixa.setEnabled(False)
            self.ui.ui_pages.btn_deletar_observacao.setEnabled(False)
            self.ui.ui_pages.btn_inserir_observacao.setEnabled(False)

        if self.modo != 'leitura':
            self.ui.ui_pages.btn_inserir_entrada_troca_dev.setEnabled(True)
            self.ui.ui_pages.btn_inserir_saida_troca_dev.setEnabled(True)
            self.ui.ui_pages.btn_deletar_id_troca_devol.setEnabled(True)
            self.ui.ui_pages.btn_inserir_entradas_n_operadora.setEnabled(True)
            self.ui.ui_pages.btn_deletar_entradas_n_operadora.setEnabled(True)
            self.ui.ui_pages.btn_inserir_despesa_cx.setEnabled(True)
            self.ui.ui_pages.btn_deletar_despesa_cx.setEnabled(True)
            self.ui.ui_pages.btn_enviar_despesa_caixa.setEnabled(True)
            self.ui.ui_pages.btn_deletar_observacao.setEnabled(True)
            self.ui.ui_pages.btn_inserir_observacao.setEnabled(True)
        
    def preencher_dados_leitura(self):
        from app.utilitarios.utilitarios import leitura_arquivo_caixa_fechado
        
        dados = leitura_arquivo_caixa_fechado(self.caixa_id)
        
        resultado_final_cx = dados['resultado_final_cx']
        troco_final_cx = dados['troco_final_cx']
        estoque_troco_cx = dados['estoque_troco_cx']
        vendas_total = dados['vendas_total']
        vendas_dinheiro_dia = dados['vendas_dinheiro_dia']
        vendas_pix_direto_cnpj = dados['vendas_pix_direto_cnpj']
        vendas_pix_direto_cpf = dados['vendas_pix_direto_cpf']
        vendas_operadoras_maq_cartao = dados['vendas_operadoras_maq_cartao']

        self.ui.ui_pages.input_resultado_fecham_cx.setText(valor_float_be_para_fe(resultado_final_cx))
        self.ui.ui_pages.input_troco_fecham_cx.setText(valor_float_be_para_fe(troco_final_cx))
        self.ui.ui_pages.input_estoque_troco_fecham_cx.setText(valor_float_be_para_fe(estoque_troco_cx))
        self.ui.ui_pages.vendas_lida_dia_fecham_cx.setText(valor_float_be_para_fe(vendas_total))
        self.ui.ui_pages.input_vendas_dinheiro_dia_fecham_cx.setText(valor_float_be_para_fe(vendas_dinheiro_dia))
        self.ui.ui_pages.input_vendas_pix_direto_cnpj_dia_fecham_cx.setText(valor_float_be_para_fe(vendas_pix_direto_cnpj))
        self.ui.ui_pages.input_vendas_pix_direto_cpf_dia_fecham_cx.setText(valor_float_be_para_fe(vendas_pix_direto_cpf))
        self.ui.ui_pages.input_total_maq_cartoes_fecham_cx.setText(valor_float_be_para_fe(vendas_operadoras_maq_cartao))

        #self.apuracao_resultado_caixa()

    def modo_completo(self):
        
        # botões
        self.ui.ui_pages.btn_apurar_resultado_caixa.show()
        self.ui.ui_pages.btn_caixa_visto.hide()
        self.ui.ui_pages.btn_enviar_fechamento_parcial_caixa.hide()
        self.ui.ui_pages.btn_enviar_fechamento_caixa.show()
        self.ui.ui_pages.vendas_lida_dia_fecham_cx.setReadOnly(True)
        
        vendas_dia = self.vendas_dia_obj.return_total_sales_day()

        if self.ui.ui_pages.opcao_cx_a_fechar.isChecked():
            vendas_dia = str(vendas_dia)
            vendas_dia = vendas_dia.replace(".",",")
            self.ui.ui_pages.vendas_lida_dia_fecham_cx.setText(vendas_dia)
            self.significacao_modo = 'caixa que será fechado definitivamente'

    def modo_pausa(self):
        
        # botões
        self.ui.ui_pages.btn_apurar_resultado_caixa.hide()
        self.ui.ui_pages.btn_caixa_visto.hide()
        self.ui.ui_pages.btn_enviar_fechamento_parcial_caixa.hide()
        self.ui.ui_pages.btn_enviar_fechamento_caixa.hide()
        self.significacao_modo = 'falta importar o arquivo do sistema EURO de vendas'
        self.ui.ui_pages.vendas_lida_dia_fecham_cx.setReadOnly(True)

    def modo_parcial(self):
        
        # botões
        self.ui.ui_pages.btn_apurar_resultado_caixa.show()
        self.ui.ui_pages.btn_caixa_visto.hide()
        self.ui.ui_pages.btn_enviar_fechamento_parcial_caixa.show()
        self.ui.ui_pages.btn_enviar_fechamento_caixa.hide()
        self.significacao_modo = 'caixa parcial que será fechado parcialmente'
        self.ui.ui_pages.vendas_lida_dia_fecham_cx.setReadOnly(False)

    def modo_outros(self):
        
        # botões
        self.ui.ui_pages.btn_apurar_resultado_caixa.hide()
        self.ui.ui_pages.btn_caixa_visto.hide()
        self.ui.ui_pages.btn_enviar_fechamento_parcial_caixa.hide()
        self.ui.ui_pages.btn_enviar_fechamento_caixa.hide()
        self.ui.ui_pages.vendas_lida_dia_fecham_cx.setReadOnly(True)
        self.significacao_modo = 'caixa que vem após o que tem que ser fechado'

    def modo_leitura(self):
        
        # botões
        self.ui.ui_pages.btn_apurar_resultado_caixa.hide()
        self.ui.ui_pages.btn_caixa_visto.show()
        self.ui.ui_pages.btn_enviar_fechamento_parcial_caixa.hide()
        self.ui.ui_pages.btn_enviar_fechamento_caixa.hide()
        self.preencher_dados_leitura()
        self.ui.ui_pages.vendas_lida_dia_fecham_cx.setReadOnly(True)
        self.significacao_modo = 'dados que serão lidos de caixa já fechado'

    def busca_troco_anterior(self):
        from app.utilitarios.utilitarios import retorna_troco_caixa_final_dia_anteiror
        trocos_caixa_anterior = retorna_troco_caixa_final_dia_anteiror(self.data_selecionada_sql)
        troco_caixa_anterior = trocos_caixa_anterior[0]
        estoque_troco_caixa_anterior = trocos_caixa_anterior[1]

        self.ui.ui_pages.input_troco_fecham_cx_anterior.setText(valor_float_be_para_fe(troco_caixa_anterior))
        self.ui.ui_pages.input_est_troco_fecham_cx_ant.setText(valor_float_be_para_fe(estoque_troco_caixa_anterior))

    def cria_lista_despesas_caixa(self):
        from app.utilitarios.utilitarios import retorna_lista_despesas_caixa
        dados_despesas = retorna_lista_despesas_caixa(self.caixa_id)
        self.lista_despesas_caixa = dados_despesas[0]
        valor_total_despesas = dados_despesas[1]

        valor_total_despesas = str(round(valor_total_despesas,2))
        valor_total_despesas = valor_total_despesas.replace(",",".")

        self.ui.ui_pages.input_total_despesas_caixa_fecham_cx.setText(valor_total_despesas)

    def contagem_troco_dinheiro(self):

        try:
            n_notas_2 = int(self.ui.ui_pages.input_notas_2.text())
        except:
            n_notas_2 = 0

        try:
            n_notas_5 = int(self.ui.ui_pages.input_notas_5.text())
        except:
            n_notas_5 = 0

        try:
            n_notas_10 = int(self.ui.ui_pages.input_notas_10.text())
        except:
            n_notas_10 = 0

        try:
            n_notas_20 = int(self.ui.ui_pages.input_notas_20.text())
        except:
            n_notas_20 = 0

        try:
            n_notas_50 = int(self.ui.ui_pages.input_notas_50.text())
        except:
            n_notas_50 = 0

        try:
            n_notas_100 = int(self.ui.ui_pages.input_notas_100.text())
        except:
            n_notas_100 = 0

        try:
            n_notas_200 = int(self.ui.ui_pages.input_notas_200.text())
        except:
            n_notas_200 = 0

        total_notas = n_notas_2 * 2 + n_notas_5 * 5 + n_notas_10 * 10 + n_notas_20 * 20 + n_notas_50 * 50 + n_notas_100 * 100 + n_notas_200 * 200
        total_notas = valor_float_be_para_fe(total_notas)       
        self.ui.ui_pages.input_total_dinheiro.setText(total_notas)
        self.fc_total_troco()

    def contagem_troco_moedas(self):

        total_moedas = 0

        try:
            n_moedas_005 = int(self.ui.ui_pages.input_moedas_005.text())
        except:
            n_moedas_005 = 0

        try:
            n_moedas_010 = int(self.ui.ui_pages.input_moedas_010.text())
        except:
            n_moedas_010 = 0

        try:
            n_moedas_025 = int(self.ui.ui_pages.input_moedas_025.text())
        except:
            n_moedas_025 = 0

        try:
            n_moedas_050 = int(self.ui.ui_pages.input_moedas_050.text())
        except:
            n_moedas_050 = 0

        try:
            n_moedas_100 = int(self.ui.ui_pages.input_moedas_100.text())
        except:
            n_moedas_100 = 0

        total_moedas = n_moedas_005 * 0.05 + n_moedas_010 * 0.10 + n_moedas_025 * 0.25 + n_moedas_050 * 0.50 + n_moedas_100 * 1.00
        
        total_moedas = valor_float_be_para_fe(total_moedas)
        self.ui.ui_pages.input_total_moedas.setText(total_moedas)

        self.fc_total_troco()

    def fc_total_troco(self):
       
        total_dinheiro = valor_str_fe_para_be(self.ui.ui_pages.input_total_dinheiro.text())        
        
        try:
            total_dinheiro = float(total_dinheiro)
        except:
            total_dinheiro = 0

        total_moedas = valor_str_fe_para_be(self.ui.ui_pages.input_total_moedas.text())

        try:
            total_moedas = float(total_moedas)
        except:
            total_moedas = 0

        self.total_troco = round(total_moedas + total_dinheiro, 2)

        self.ui.ui_pages.input_total_troco.setText(valor_float_be_para_fe(self.total_troco))

    def enviando_facilitador_troco_para_fechamento_caixa(self):

        if not self.ui.ui_pages.opcao_estoque_troco_cx.isChecked() and not self.ui.ui_pages.opcao_troco_cx.isChecked():
            self.show_message_warning('Selecionar','Necessita selecionar para onde mandar o facilitador de troco.')
            return
        
        if self.ui.ui_pages.opcao_estoque_troco_cx.isChecked():
            self.ui.ui_pages.input_estoque_troco_fecham_cx.setText(valor_float_be_para_fe(self.total_troco))

        if self.ui.ui_pages.opcao_troco_cx.isChecked():
            self.ui.ui_pages.input_troco_fecham_cx.setText(valor_float_be_para_fe(self.total_troco))

        self.apuracao_resultado_caixa()

    def show_message_answer(self, titulo, message):
        resposta = QMessageBox.question(self, titulo, message, QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if resposta == 16384:
            resposta = True

        if resposta == 65536:
            resposta = False

        return resposta

    def show_message_warning(self, titulo, message):
        QMessageBox.warning(self, titulo, message)

    def show_message_info(self, titulo, message):
        QMessageBox.information(self, titulo, message)

    def troco_caixa_button(self):
        
        if self.name_user == '':
            self.show_message_warning("Login", "Usuário não logado.")
            return

        if self.choiced_date == False:
            self.show_message_warning("Data", "Data de referência precisa ser escolhida.")
            return

        if self.modo == 'leitura' or self.modo == 'outros':
            self.show_message_info('Modo incompatível','Somente para datas de fechamento de Caixa(total ou parcial).')
            return
        
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.troco_cx)
        self.ui.top_bar_right_label.setText("| Troco de Caixa")

    def fechamento_caixa_button(self):
        
        if self.name_user == '':
            self.show_message_warning("Login", "Usuário não logado.")
            return

        if self.choiced_date == False:
            self.show_message_warning("Data", "Data de referência precisa ser escolhida.")
            return
                
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.fecham_cx)
        self.ui.top_bar_right_label.setText("| Fechamento de Caixa")

    def escolha_data_cx_button(self):

        self.limpa_dados_fechamento_caixa()

        self.choiced_date = False
        
        if self.name_user == '':
            self.show_message_warning("Login", "Usuário não logado.")
            return
        
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.escolha_data_cx)
        self.ui.top_bar_right_label.setText("| Escolha Data de Caixa")

    def entrada_n_operadora_button(self):
        
        if self.name_user == '':
            self.show_message_warning("Login", "Usuário não logado.")
            return
        
        if self.choiced_date == False:
            self.show_message_warning("Data", "Data de referência precisa ser escolhida.")
            return
        
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_insercao_entradas_nao_operadora)
        self.ui.top_bar_right_label.setText("| Entradas Não Máquina")

    def trocas_devolucoes_button(self):
        
        if self.name_user == '':
            self.show_message_warning("Login", "Usuário não logado.")
            return
        
        if self.choiced_date == False:
            self.show_message_warning("Data", "Data de referência precisa ser escolhida.")
            return
        
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.trocas_devolucoes)
        self.ui.top_bar_right_label.setText("| Trocas e Devoluções")

    def observacao_cx_button(self):
        
        if self.name_user == '':
            self.show_message_warning("Login", "Usuário não logado.")
            return
        
        if self.choiced_date == False:
            self.show_message_warning("Data", "Data de referência precisa ser escolhida.")
            return
        
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.observacao_cx)
        self.ui.top_bar_right_label.setText("| Observações de Caixa")

    def ver_despesas_cx_button(self):
        
        if self.name_user == '':
            self.show_message_warning("Login", "Usuário não logado.")
            return
        
        if self.choiced_date == False:
            self.show_message_warning("Data", "Data de referência precisa ser escolhida.")
            return
        
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.ver_despesas_cx)
        self.ui.top_bar_right_label.setText("| Ver Despesas de Caixa")

        self.cria_lista_despesas_caixa()
        n_linhas = len(self.lista_despesas_caixa)

        self.model_table_ver_despesas = QStandardItemModel(n_linhas,3)
        self.model_table_ver_despesas.setHorizontalHeaderLabels(['ID','descricao','valor'])

        self.adicionar_dados_tabela_ver_despesas()

        self.ui.ui_pages.table_ver_despesas.setModel(self.model_table_ver_despesas)

        #self.ui.ui_pages.table_ver_despesas.horizontalHeader().setStretchLastSection(True)
        self.ui.ui_pages.table_ver_despesas.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

    def inserir_despesas_cx_button(self):

        if self.modo == 'parcial' or self.modo == 'outros' or self.modo == 'completo':
            self.ui.pages.setCurrentWidget(self.ui.ui_pages.inserir_despesas_cx)
            self.ui.top_bar_right_label.setText("| Inserir Despesas de Caixa")

        if self.modo == 'leitura':
            self.show_message_warning("Caixa já fechado","Caixa já fechado. Não pode haver alterações.")
            return

    def adicionar_dados_tabela_ver_despesas(self):
        
        for row, linha_dados in enumerate(self.lista_despesas_caixa):            
            
            item_1 = QStandardItem(str(linha_dados['id']))
            self.model_table_ver_despesas.setItem(row, 0, item_1)
            
            item_2 = QStandardItem(linha_dados['descricao'])
            self.model_table_ver_despesas.setItem(row, 1, item_2)
            
            item_3 = QStandardItem((str(linha_dados['valor'])).replace(".",","))
            self.model_table_ver_despesas.setItem(row, 2, item_3)

    def login_button(self):
        from app.utilitarios.utilitarios import entra_code_user_return_name_user
        import time
        
        self.code_user = self.ui.ui_pages.input_user_code.text()
        
        try:
            self.code_user = int(self.code_user)
        except:
            self.code_user = 0

        if self.code_user != 0:
            self.name_user = entra_code_user_return_name_user(self.code_user)
        
        if self.code_user == 0:
            self.name_user = ''

        if self.name_user != '':
            self.ui.ui_pages.lbl_ola.show()            

            if self.code_user == 96:
                self.ui.ui_pages.nome_usuario_login.setStyleSheet("font: 700 14pt 'Segoe UI'; color: rgb(255,0,0);")
            if self.code_user != 96:
                self.ui.ui_pages.nome_usuario_login.setStyleSheet("font: 700 14pt 'Segoe UI'; color: 'lightblue';")

            self.ui.ui_pages.nome_usuario_login.setText(f"{self.name_user}")
            self.ui.ui_pages.btn_selection_date.show()            
            self.ui.ui_pages.input_user_name.setText(f"{self.name_user}")

            self.ui.ui_pages.btn_selection_date.clicked.connect(self.escolha_data_cx_button)

        if self.name_user == '':
            self.ui.ui_pages.nome_usuario_login.setText(f"Usuário não cadastrado.")
            self.ui.ui_pages.input_user_code.setText('')
            return

        self.ui.ui_pages.input_user_code.setText('')

        self.ui.ui_pages.btn_login.hide()
        self.ui.ui_pages.input_user_code.hide()
        self.ui.ui_pages.label_login.hide()

    def toggle_button(self):
        # get menu width
        menu_width = self.ui.left_menu.width()

        # check width
        width = width_min = 50
        width_max = 180

        if menu_width == width_min:
            width = width_max

        # Start animation
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.OutCirc)
        self.animation.start()

    def opcao_caixa_outros(self):
        from app.utilitarios.utilitarios import retorna_data_para_fechar_caixa
        from app.utilitarios.datas.retornos_partes_da_data import retorna_ano_data, retorna_dia_data, retorna_mes_data

        data_a_fechar_sql = retorna_data_para_fechar_caixa()

        dia_a_fechar = retorna_dia_data(data_a_fechar_sql)
        mes_a_fechar = retorna_mes_data(data_a_fechar_sql)
        ano_a_fechar = retorna_ano_data(data_a_fechar_sql)

        data_a_fechar_qdate = QDate(ano_a_fechar, mes_a_fechar, dia_a_fechar)

        self.data_atual()

        self.ui.ui_pages.calendario_widget.setMinimumDate(data_a_fechar_qdate)
        self.ui.ui_pages.calendario_widget.setMaximumDate(self.agora_qdate)

    def opcao_caixa_a_fechar(self):
        from app.utilitarios.utilitarios import retorna_data_para_fechar_caixa
        from app.utilitarios.datas.retornos_partes_da_data import retorna_ano_data, retorna_dia_data, retorna_mes_data

        data_a_fechar_sql = retorna_data_para_fechar_caixa()

        dia_a_fechar = retorna_dia_data(data_a_fechar_sql)
        mes_a_fechar = retorna_mes_data(data_a_fechar_sql)
        ano_a_fechar = retorna_ano_data(data_a_fechar_sql)

        data_a_fechar_qdate = QDate(ano_a_fechar, mes_a_fechar, dia_a_fechar)

        self.ui.ui_pages.calendario_widget.setMinimumDate(data_a_fechar_qdate)
        self.ui.ui_pages.calendario_widget.setMaximumDate(data_a_fechar_qdate)

    def opcao_caixa_fechado(self):
        from app.utilitarios.utilitarios import retorna_data_max_caixas_fechados, retorna_data_min_caixas_fechados
        from app.utilitarios.datas.retornos_partes_da_data import retorna_ano_data, retorna_dia_data, retorna_mes_data

        data_min = retorna_data_min_caixas_fechados()
        data_max = retorna_data_max_caixas_fechados()

        dia_min = retorna_dia_data(data_min)
        mes_min = retorna_mes_data(data_min)
        ano_min = retorna_ano_data(data_min)

        dia_max = retorna_dia_data(data_max)
        mes_max = retorna_mes_data(data_max)
        ano_max = retorna_ano_data(data_max)
        
        data_min_qdate = QDate(ano_min, mes_min, dia_min)
        data_max_qdate = QDate(ano_max, mes_max, dia_max)

        self.ui.ui_pages.calendario_widget.setMinimumDate(data_min_qdate)
        self.ui.ui_pages.calendario_widget.setMaximumDate(data_max_qdate)

    def limpar_entradas_n_maquina(self):
        self.ui.ui_pages.input_valor_entradas_n_operadora.setText('')
        self.ui.ui_pages.comboBox_entradas_n_operadora.setCurrentIndex(0)
        self.ui.ui_pages.input_id_deletar_entradas_n_operadora.setText('')

    def limpar_campos_facilitador_troco_cx(self):
        
        # moedas
        self.ui.ui_pages.input_moedas_005.clear()
        self.ui.ui_pages.input_moedas_010.clear()
        self.ui.ui_pages.input_moedas_025.clear()
        self.ui.ui_pages.input_moedas_050.clear()
        self.ui.ui_pages.input_moedas_100.clear()

        # notas
        self.ui.ui_pages.input_notas_2.clear()
        self.ui.ui_pages.input_notas_5.clear()
        self.ui.ui_pages.input_notas_10.clear()
        self.ui.ui_pages.input_notas_20.clear()
        self.ui.ui_pages.input_notas_50.clear()
        self.ui.ui_pages.input_notas_100.clear()
        self.ui.ui_pages.input_notas_200.clear()

        self.ui.ui_pages.input_total_moedas.clear()
        self.ui.ui_pages.input_total_dinheiro.clear()
        self.ui.ui_pages.input_total_troco.clear()

    def verificador_first_time(self):
        # verifica se bd existe

        print('verificações')
        self.processar_atualizacoes_pendentes()

        from utils_banco_dados.conexao import Conexao
        conexao = Conexao()

        command = "SELECT COUNT(*) FROM usuarios;"

        try:
            result = conexao.bd_fetchall(command)
        except:
            result = 0
        
        if result != 0:
            self.first_time = False
            print(f'Já existe. \nNO first time')
            return
        
        if result == 0:
            self.first_time = True
            print('YES first time')
            return

    def inserir_entradas_n_operadora(self):

        from app.utilitarios.utilitarios import inserir_entrada_n_operadora_maq
        
        index = self.ui.ui_pages.comboBox_entradas_n_operadora.currentIndex()

        if index == 0:
            self.show_message_info('ERRO','Tipo de entrada necessita ser escolhido.')
            return
                
        id_tipo_entrada = self.ui.ui_pages.comboBox_entradas_n_operadora.itemData(index)

        valor = valor_str_fe_para_be(self.ui.ui_pages.input_valor_entradas_n_operadora.text())

        if valor == '' or valor == 0:
            self.show_message_warning("Digitar","Precisa digitar o valor da entrada.")
            return

        insercao = inserir_entrada_n_operadora_maq(self.caixa_id, self.code_user, valor, id_tipo_entrada)

        if insercao == True:
            self.show_message_info('OK','Inserção feita.')

        if insercao == False:
            self.show_message_warning('ERRO','Não foi incluso no Banco de Dados. Algum erro')

        self.busca_entradas_n_operadora()
        self.apuracao_resultado_caixa()
        self.limpar_entradas_n_maquina()
        return

    def deletar_entradas_n_operadora(self):
        from app.utilitarios.utilitarios import deletar_entrada_n_operadora_maq

        id_entrada_n_operadora = int(valor_str_fe_para_be(self.ui.ui_pages.input_id_deletar_entradas_n_operadora.text()))

        resposta = self.show_message_answer('Confimação',f'Realmente quer deletar a entrada de ID: {id_entrada_n_operadora} ?')

        if resposta == False:            
            self.ui.ui_pages.input_id_deletar_entradas_n_operadora.setText('')
            self.show_message_info('Info','Nada será deletado.')
            return

        delecao = deletar_entrada_n_operadora_maq(id_entrada_n_operadora)

        if delecao == True:
            self.show_message_info('OK','Entrada n Operadora deletada.')

        if delecao == False:
            self.show_message_warning('ERRO','Algo deu errado com a deleção da Entrada não Operadora.')

        self.busca_entradas_n_operadora()
        self.apuracao_resultado_caixa()
        self.limpar_entradas_n_maquina()
        return

    def processar_atualizacoes_pendentes(self):
        import os
        print('verificando caminhos para a importação do updates.json')
        
        # Caminhos
        
        db_path = os.path.join(r"C:\marcio\programas\app_cashier\database_app\app_cashier.db")
        json_path = os.path.join(r"C:\marcio\programas\app_cashier\database_app\updates.json")
       
        if not os.path.exists(json_path):
            print('updates.json não existe')
            print()
            return False
        
        print("[Atualizações] Processando...")
        
        conn = None
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                updates = json.load(f)
            
            # Conexão direta (mais segura)
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("BEGIN TRANSACTION")
            
            total = 0
            
            # Tabelas
            tabelas = [
                ('observacoes_caixa', updates['updates']['observacoes_caixa']),
                ('dados_fechamentos_caixa', updates['updates']['dados_fechamentos_caixa']),
                ('despesas_caixa', updates['updates']['despesas_caixa']),
                ('fechamentos_parciais_caixa', updates['updates']['fechamentos_parciais_caixa']),
            ]
            
            for tabela, ids in tabelas:
                if ids:
                    for id_reg in ids:
                        cursor.execute(f"UPDATE {tabela} SET read_app_parent = 1 WHERE id = ?", (id_reg,))
                    total += len(ids)
                    print(f"[Atualizações] ✅ {tabela}: {len(ids)} registros")
            
            conn.commit()
            os.remove(json_path)
            print(f"[Atualizações] ✅ Total: {total} registros atualizados")
            return True
            
        except Exception as e:
            print(f"[Atualizações] ❌ Erro: {e}")
            if conn:
                conn.rollback()
            return False
        finally:
            if conn:
                conn.close()

def valor_str_fe_para_be(valor):
    
    if valor == '' or valor == None:
        return 0.00
    
    valor = str(valor)
    valor = valor.replace(",",".")
    
    try:
        new_valor = float(valor)
    except:
        new_valor = 0.00

    return new_valor

def valor_float_be_para_fe(valor):
    valor = str(round(valor,2))
    new_valor = valor.replace(".",",")
    nova_lista = new_valor.split(",")
    
    if len(nova_lista) == 1:
        new_valor += ',00'
    
    if len(nova_lista) == 2 and len(nova_lista[1]) == 1:
        new_valor += '0'    

    return str(new_valor)

def pasta_banco_dados():
    from pathlib import Path
    caminho_base = Path().absolute()
    caminho_pastas = Path(caminho_base).joinpath('database_app')
    caminho_pastas.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    pasta_banco_dados()
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
