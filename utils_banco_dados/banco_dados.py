class Banco_Dados:

    def __init__(self):        
        self.conectar()
        self.tabela_usuarios()
        self.tabela_despesas()
        self.tabela_dados_fechamentos_caixa()
        self.tabela_fechamentos_parciais_caixa()
        self.tabela_despesas_caixa()
        self.tabela_observacoes_caixa()
        self.tabela_vendas_dia()
        self.tabela_trocas_devolucoes_dia()
        self.tabela_tipo_entrada_n_operadora_maq()
        self.tabela_entradas_n_operadora_maq()
        self.mostrar_tudo()
        self.desconectar()

    def conectar(self):
        from utils_banco_dados.conexao import Conexao
        self.conexao = Conexao()  

    def tabela_usuarios(self):

        comand = "CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)"
        self.conexao.bd_commit(comand)

        comand = "SELECT COUNT(*) FROM usuarios"
        count = self.conexao.bd_fetchall(comand)[0][0]
        
        if count == 0:
            # Inserir dados iniciais apenas se a tabela estiver vazia
            dados_iniciais = [
                (4,"Marcio Suconic"),
                (26,"Veronica Suconic"),
                (45,"Beatriz Suconic"),
                (37,"Gustavo"),
                (96,"Yara"),
                (106,"Matheus")
            ]

            for id,nome in dados_iniciais:
                comand = f"INSERT INTO usuarios (`id`, `nome`) VALUES ({id}, '{nome}')"
                self.conexao.bd_commit(comand)
           
            comand = "SELECT COUNT(*) FROM usuarios"
            count = self.conexao.bd_fetchall(comand)[0][0]
            
            print(f"Tabela Usuários inseridos! ({count} inseridos.)")

        else:
            print(f"Tabela Usuários já contém dados ({count} registros). Nenhum dado inicial inserido.")

    def tabela_despesas(self):

        comand = "CREATE TABLE IF NOT EXISTS despesas (id INTEGER PRIMARY KEY AUTOINCREMENT, despesa TEXT NOT NULL)"
        self.conexao.bd_commit(comand)

        comand = "SELECT COUNT(*) FROM despesas"
        count = self.conexao.bd_fetchall(comand)[0][0]
        
        if count == 0:
            # Inserir dados iniciais apenas se a tabela estiver vazia

            dados_iniciais = [
                (1, "Retirada Marcio"),
                (2, "Despesas com Àgua e afins"),
                (3, "Funcionários - Salários"),
                (4, "Limpeza Vitrine"),
                (5, "Materiais Limpeza"),
                (6, "Materiais Escritório"),
                (7, "Funcionários - Condução"),
                (8, "Funcionários - Vale"),
                (9, "Materiais para manutenção da loja"),
                (10, "Funcionários - pagamento de feriado"),
                (11, "Miniaturas - Fornecedor")
            ]

            for id, despesa in dados_iniciais:
                comand = f"INSERT INTO despesas (id, despesa) VALUES ({id}, '{despesa}')"
                self.conexao.bd_commit(comand)

            comand = "SELECT COUNT(*) FROM despesas"
            count = self.conexao.bd_fetchall(comand)[0][0]
            
            print(f"Tabela Despesas inseridos! ({count} inseridos.)")
        else:
            print(f"Tabela Despesas já contém dados ({count} registros). Nenhum dado inicial inserido.")

    def tabela_dados_fechamentos_caixa(self):

        comand = """CREATE TABLE IF NOT EXISTS dados_fechamentos_caixa (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data_caixa DATE NOT NULL,
                data_fechamento DATE NOT NULL default '2025-07-31',
                hora INTEGER NOT NULL default 0,
                minutos INTEGER NOT NULL default 0,
                usuario_id INTEGER NOT NULL,
                resultado_final_cx REAL NOT NULL,
                troco_final_cx REAL NOT NULL,
                estoque_troco_cx REAL NOT NULL,
                vendas_total REAL NOT NULL,
                vendas_dinheiro_dia REAL NOT NULL,
                vendas_pix_direto_cnpj REAL NOT NULL default 0.00,
                vendas_pix_direto_cpf REAL NOT NULL default 0.00,
                vendas_operadoras_maq_cartao REAL NOT NULL,
                result_trocas_devs_dinheiro REAL NOT NULL default 0.00,
                result_trocas_devs_debito REAL NOT NULL default 0.00,
                result_trocas_devs_credito REAL NOT NULL default 0.00,
                result_trocas_devs_produtos REAL NOT NULL default 0.00,
                caixa_fechado INTEGER NOT NULL default 0,
                dia_loja_fechada INTEGER NOT NULL default 0,
                read_app_parent INTEGER NOT NULL default 0,
                FOREIGN KEY (usuario_id)
                    REFERENCES usuarios(id)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
            )
        """
        self.conexao.bd_commit(comand)

        comand = "SELECT COUNT(*) FROM dados_fechamentos_caixa"
        count = self.conexao.bd_fetchall(comand)[0][0]

        if count == 0:

            comand = "INSERT INTO dados_fechamentos_caixa (id, data_caixa, data_fechamento, usuario_id, resultado_final_cx, troco_final_cx, estoque_troco_cx, vendas_total, vendas_dinheiro_dia, vendas_pix_direto_cnpj, vendas_operadoras_maq_cartao, caixa_fechado, vendas_pix_direto_cpf) VALUES (458,'2025-10-31','2025-11-01' ,96, 0.00, 1719.71, 100.00, 4432.01, 2.71, 0.00, 4430.68, 1, 0.00)"
            self.conexao.bd_commit(comand)

            comand = "INSERT INTO dados_fechamentos_caixa (id, data_caixa, data_fechamento, usuario_id, resultado_final_cx, troco_final_cx, estoque_troco_cx, vendas_total, vendas_dinheiro_dia, vendas_pix_direto_cnpj, vendas_operadoras_maq_cartao, caixa_fechado, vendas_pix_direto_cpf) VALUES (459,'2025-11-01','2025-11-02' ,96, 0.00, 187.35, 100.00, 3521.31, 39.91, 0.00, 3481.40, 1, 0.00)"
            self.conexao.bd_commit(comand)

            comand = "INSERT INTO dados_fechamentos_caixa (id, data_caixa, data_fechamento, usuario_id, resultado_final_cx, troco_final_cx, estoque_troco_cx, vendas_total, vendas_dinheiro_dia, vendas_pix_direto_cnpj, vendas_operadoras_maq_cartao, caixa_fechado, vendas_pix_direto_cpf) VALUES (460,'2025-11-02','2025-11-03' ,96, 0.15, 181.40, 100.00, 4000.00, 18.90, 0.00, 3981.10, 1, 0.00)"
            self.conexao.bd_commit(comand)

            comand = "INSERT INTO dados_fechamentos_caixa (id, data_caixa, data_fechamento, usuario_id, resultado_final_cx, troco_final_cx, estoque_troco_cx, vendas_total, vendas_dinheiro_dia, vendas_pix_direto_cnpj, vendas_operadoras_maq_cartao, caixa_fechado, vendas_pix_direto_cpf) VALUES (461,'2025-11-03','2025-11-04' ,96, -0.02, 181.40, 100.00, 1366.52, 0.02, 199.00, 1167.50, 1, 0.00)"
            self.conexao.bd_commit(comand)

            comand = "INSERT INTO dados_fechamentos_caixa (id, data_caixa, data_fechamento, usuario_id, resultado_final_cx, troco_final_cx, estoque_troco_cx, vendas_total, vendas_dinheiro_dia, vendas_pix_direto_cnpj, vendas_operadoras_maq_cartao, caixa_fechado, vendas_pix_direto_cpf) VALUES (462,'2025-11-04','2025-11-05' ,96, -0.04, 191.20, 100.00, 889.14, 9.84, 0.00, 879.30, 1, 0.00)"
            self.conexao.bd_commit(comand)

            comand = "INSERT INTO dados_fechamentos_caixa (id, data_caixa, data_fechamento, usuario_id, resultado_final_cx, troco_final_cx, estoque_troco_cx, vendas_total, vendas_dinheiro_dia, vendas_pix_direto_cnpj, vendas_operadoras_maq_cartao, caixa_fechado, vendas_pix_direto_cpf) VALUES (463,'2025-11-05','2025-11-06' ,96, 0.00, 191.20, 100.00, 2422.30, 1269.00, 0.00, 1153.30, 1, 0.00)"
            self.conexao.bd_commit(comand)

            comand = "INSERT INTO dados_fechamentos_caixa (id, data_caixa, data_fechamento, usuario_id, resultado_final_cx, troco_final_cx, estoque_troco_cx, vendas_total, vendas_dinheiro_dia, vendas_pix_direto_cnpj, vendas_operadoras_maq_cartao, caixa_fechado, vendas_pix_direto_cpf) VALUES (464,'2025-11-06','2025-11-07' ,96, 0.00, 90.15, 100.00, 1242.10, 3.70, 0.00, 1238.40, 1, 0.00)"
            self.conexao.bd_commit(comand)

            comand = "INSERT INTO dados_fechamentos_caixa (id, data_caixa, data_fechamento, usuario_id, resultado_final_cx, troco_final_cx, estoque_troco_cx, vendas_total, vendas_dinheiro_dia, vendas_pix_direto_cnpj, vendas_operadoras_maq_cartao, caixa_fechado, vendas_pix_direto_cpf) VALUES (465,'2025-11-07','2025-11-08' ,96, -0.01, 90.15, 100.00, 1750.81, 0.01, 0.00, 1750.80, 1, 0.00)"
            self.conexao.bd_commit(comand)

            comand = "INSERT INTO dados_fechamentos_caixa (id, data_caixa, data_fechamento, usuario_id, resultado_final_cx, troco_final_cx, estoque_troco_cx, vendas_total, vendas_dinheiro_dia, vendas_pix_direto_cnpj, vendas_operadoras_maq_cartao, caixa_fechado, vendas_pix_direto_cpf) VALUES (466,'2025-11-08','2025-11-09' ,96, 0.00, 614.15, 100.00, 6097.80, 524, 0.00, 5573.80, 1, 0.00)"
            self.conexao.bd_commit(comand)

            comand = "INSERT INTO dados_fechamentos_caixa (id, data_caixa, data_fechamento, usuario_id, resultado_final_cx, troco_final_cx, estoque_troco_cx, vendas_total, vendas_dinheiro_dia, vendas_pix_direto_cnpj, vendas_operadoras_maq_cartao, caixa_fechado, vendas_pix_direto_cpf) VALUES (467,'2025-11-09', '2025-11-10',96, 0.00, 679.95, 100.00, 1560.40, 65.80, 0.00, 1494.60, 1, 0.00)"
            self.conexao.bd_commit(comand)

            comand = "INSERT INTO dados_fechamentos_caixa (id, data_caixa, data_fechamento, usuario_id, resultado_final_cx, troco_final_cx, estoque_troco_cx, vendas_total, vendas_dinheiro_dia, vendas_pix_direto_cnpj, vendas_operadoras_maq_cartao, caixa_fechado, vendas_pix_direto_cpf) VALUES (468,'2025-11-10', '2025-11-11',96, 0.00, 889.97, 100.00, 3912.62, 210.02, 0.00, 3702.60, 1, 0.00)"
            self.conexao.bd_commit(comand)

            comand = "INSERT INTO dados_fechamentos_caixa (id, data_caixa, data_fechamento, usuario_id, resultado_final_cx, troco_final_cx, estoque_troco_cx, vendas_total, vendas_dinheiro_dia, vendas_pix_direto_cnpj, vendas_operadoras_maq_cartao, caixa_fechado, vendas_pix_direto_cpf) VALUES (469, '2025-11-11', '2025-11-12',96, 0.00, 376.30, 100.00, 1057.81, 50.01, 0.00, 1007.80, 1, 0.00)"
            self.conexao.bd_commit(comand)

            comand = "INSERT INTO dados_fechamentos_caixa (id, data_caixa, data_fechamento, usuario_id, resultado_final_cx, troco_final_cx, estoque_troco_cx, vendas_total, vendas_dinheiro_dia, vendas_pix_direto_cnpj, vendas_operadoras_maq_cartao, caixa_fechado, vendas_pix_direto_cpf) VALUES (470,'2025-11-12', '2025-11-13',96, 1.99, 815.10, 100.00, 2422.11, 436.81, 0.00, 1983.50, 1, 0.00)"
            self.conexao.bd_commit(comand)           
            
            comand = "SELECT COUNT(*) FROM dados_fechamentos_caixa"            
            count = self.conexao.bd_fetchall(comand)[0][0]
            
            print(f"Tabela Dados de Fechamentos de Caixas iniciais inseridos! ({count} inseridos.)")

        else:
            print(f"Tabela Dados de Fechamentos de Caixas já contém dados ({count} registros). Nenhum dado inicial inserido.")

    def tabela_despesas_caixa(self):
        
        comand = "CREATE TABLE IF NOT EXISTS despesas_caixa (id INTEGER PRIMARY KEY AUTOINCREMENT, descricao_despesa TEXT, valor_despesa REAL NOT NULL, despesa_id INTEGER NOT NULL, caixa_id INTEGER NOT NULL, read_app_parent INTEGER NOT NULL default 0, FOREIGN KEY (despesa_id) REFERENCES despesas(id) ON DELETE CASCADE ON UPDATE CASCADE, FOREIGN KEY (caixa_id) REFERENCES dados_fechamentos_caixa(id) ON DELETE CASCADE ON UPDATE CASCADE)"
        self.conexao.bd_commit(comand)

        comand = "SELECT COUNT(*) FROM despesas_caixa"
        count = self.conexao.bd_fetchall(comand)[0][0]

        if count == 0:
            command = "INSERT INTO despesas_caixa (descricao_despesa, valor_despesa, despesa_id, caixa_id) VALUES ('ajuste cx', 1572.27, 1, 459);"
            self.conexao.bd_commit(command)

            command = "INSERT INTO despesas_caixa (descricao_despesa, valor_despesa, despesa_id, caixa_id) VALUES ('ajuste cx', 25, 1, 460);"
            self.conexao.bd_commit(command)

            command = "INSERT INTO despesas_caixa (descricao_despesa, valor_despesa, despesa_id, caixa_id) VALUES ('salario funcionarios', 1269, 3, 463);"
            self.conexao.bd_commit(command)

            command = "INSERT INTO despesas_caixa (descricao_despesa, valor_despesa, despesa_id, caixa_id) VALUES ('ajuste cx', 104.75, 1, 464);"
            self.conexao.bd_commit(command)

            command = "INSERT INTO despesas_caixa (descricao_despesa, valor_despesa, despesa_id, caixa_id) VALUES ('ajuste cx', 563.68, 1, 469);"
            self.conexao.bd_commit(command)

            command = "INSERT INTO despesas_caixa (descricao_despesa, valor_despesa, despesa_id, caixa_id) VALUES ('condução Matheus', 180, 7, 499);"
            self.conexao.bd_commit(command)

            command = "INSERT INTO despesas_caixa (descricao_despesa, valor_despesa, despesa_id, caixa_id) VALUES ('ajuste cx', 92.80, 1, 499);"
            self.conexao.bd_commit(command)

        comand = "SELECT COUNT(*) FROM despesas_caixa"
        count = self.conexao.bd_fetchall(comand)[0][0]

        print(f"Há {count} registro(s) na Tabela Despesas de Caixa")

    def tabela_observacoes_caixa(self):
        comand = "CREATE TABLE IF NOT EXISTS observacoes_caixa (id INTEGER PRIMARY KEY AUTOINCREMENT, observacao_caixa TEXT NOT NULL, caixa_id INTEGER NOT NULL, read_app_parent INTEGER NOT NULL default 0 , FOREIGN KEY (caixa_id) REFERENCES dados_fechamentos_caixa(id) ON DELETE CASCADE ON UPDATE CASCADE)"
        self.conexao.bd_commit(comand)

        comand = "SELECT COUNT(*) FROM observacoes_caixa"
        count = self.conexao.bd_fetchall(comand)[0][0]

        print(f"Há {count} registro(s) na Tabela Observações de Caixa")

    def tabela_vendas_dia(self):
        comand = "CREATE TABLE IF NOT EXISTS vendas_dia (id INTEGER PRIMARY KEY AUTOINCREMENT, data DATE, vendas_dia REAL NOT NULL, read_app_parent INTEGER NOT NULL default 0)"
        self.conexao.bd_commit(comand)

        comand = "SELECT COUNT(*) FROM vendas_dia"
        count = self.conexao.bd_fetchall(comand)[0][0]

        print(f"Há {count} registro(s) na Tabela Vendas Dia")

    def tabela_trocas_devolucoes_dia(self):
        #SELECT `id`, `codigo`, `forma`, `valor`, `entrada_saida` FROM trocas_devolucoes_dia WHERE `caixa_id`=471;
        # entrada = 'E', saida = 'S'
        comand = "CREATE TABLE IF NOT EXISTS trocas_devolucoes_dia (id INTEGER PRIMARY KEY AUTOINCREMENT, caixa_id INTEGER NOT NULL, num_pedido_sistema INTEGER, codigo_produto TEXT, tipo_ent_ou_sai TEXT, valor REAL NOT NULL, entrada_ou_saida TEXT NOT NULL, relevancia_caixa INTEGER NOT NULL default 0,read_app_parent INTEGER NOT NULL default 0, FOREIGN KEY (caixa_id) REFERENCES dados_fechamentos_caixa(id) ON DELETE CASCADE ON UPDATE CASCADE);"
        self.conexao.bd_commit(comand)

        comand = "SELECT COUNT(*) FROM trocas_devolucoes_dia"
        count = self.conexao.bd_fetchall(comand)[0][0]

        print(f"Há {count} registro(s) na Tabela Trocas e Devoluções")

    def tabela_fechamentos_parciais_caixa(self):
        
        tabela = 'fechamentos_parciais_caixa'

        command = f"""CREATE TABLE IF NOT EXISTS {tabela} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                caixa_id INTEGER NOT NULL,
                data DATE NOT NULL,
                hora INTEGER NOT NULL default 0,
                minutos INTEGER NOT NULL default 0,
                usuario_id INTEGER NOT NULL,
                resultado_final_cx REAL NOT NULL,
                troco_final_cx REAL NOT NULL,
                estoque_troco_cx REAL NOT NULL,
                vendas_total REAL NOT NULL,
                vendas_dinheiro_dia REAL NOT NULL,
                vendas_pix_direto_cnpj REAL NOT NULL default 0.00,
                vendas_pix_direto_cpf REAL NOT NULL default 0.00,
                vendas_operadoras_maq_cartao REAL NOT NULL,                
                result_trocas_devs_dinheiro REAL NOT NULL default 0.00,
                result_trocas_devs_debito REAL NOT NULL default 0.00,
                result_trocas_devs_credito REAL NOT NULL default 0.00,
                result_trocas_devs_produtos REAL NOT NULL default 0.00,
                read_app_parent INTEGER NOT NULL default 0,

                FOREIGN KEY (usuario_id) 
                    REFERENCES usuarios(id)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE,
                FOREIGN KEY (CAIXA_id) 
                    REFERENCES dados_fechamentos_caixa(id)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
            );
        """
        self.conexao.bd_commit(command)

        comand = f"SELECT COUNT(*) FROM {tabela}"
        count = self.conexao.bd_fetchall(comand)[0][0]

        print(f"Há {count} registro(s) na Tabela: {tabela}")

    def tabela_tipo_entrada_n_operadora_maq(self):

        dados = [
            [1,"dinheiro"],
            [2,"PIX direto CNPJ"],
            [3,"PIX diretor CPF"]
        ]

        tabela = 'tipos_entradas_n_operadora_maq'

        command = f"""
                CREATE TABLE IF NOT EXISTS {tabela} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo_entrada TEXT NOT NULL
                );
        """
        self.conexao.bd_commit(command)

        command = f"SELECT COUNT(*) FROM {tabela}"
        count = self.conexao.bd_fetchall(command)[0][0]

        if count == 0:
            for item in dados:
                command = f"INSERT INTO {tabela} (id, tipo_entrada) VALUES ({item[0]},'{item[1]}');"
                self.conexao.bd_commit(command)

        command = f"SELECT COUNT(*) FROM {tabela}"
        count = self.conexao.bd_fetchall(command)[0][0]

        print(f"Há {count} registro(s) na Tabela: {tabela}")

    def tabela_entradas_n_operadora_maq(self):

        tabela = 'entradas_n_operadora_maq'

        command = f""" 
                CREATE TABLE IF NOT EXISTS {tabela} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                caixa_id INTEGER NOT NULL,
                usuario_id INTEGER NOT NULL,
                valor REAL NOT NULL,
                tipo_entrada_n_operadora_maq INTEGER NOT NULL,
                read_app_parent INTEGER NOT NULL default 0,                
                FOREIGN KEY (usuario_id) 
                    REFERENCES usuarios(id)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE,
                FOREIGN KEY (caixa_id) 
                    REFERENCES dados_fechamentos_caixa(id)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE,
                FOREIGN KEY (tipo_entrada_n_operadora_maq) 
                    REFERENCES tipo_entrada_n_operadora_maq(id)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
            )
        """
        self.conexao.bd_commit(command)

        command = f"SELECT COUNT(*) FROM {tabela}"
        count = self.conexao.bd_fetchall(command)[0][0]

        print(f"Há {count} registro(s) na Tabela: {tabela}")

    def mostrar_tudo(self):

        command = """
            SELECT * FROM sqlite_master WHERE type='table';
        """

        result = self.conexao.bd_fetchall(command)

        for item in result:
            print(item[0],item[1])

    def desconectar(self):
        self.conexao.desconectar()
