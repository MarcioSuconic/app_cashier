from utils_banco_dados.conexao import Conexao
conexao = Conexao()

def entra_code_user_return_name_user(code_user):
    code_user = int(code_user)
    
    comand = f"SELECT `nome` FROM usuarios WHERE `id` = {code_user}"
    try:
        nome = conexao.bd_fetchall(comand)[0][0]
    except:
        nome = ''
    return nome

def entra_data_sql_retorna_caixa_id(data_sql):

    comand = f"SELECT `id` FROM dados_fechamentos_caixa WHERE `data_caixa` = '{data_sql}';"
    result = conexao.bd_fetchall(comand)
    return result[0][0]

def proximo_id_dados_fechamento_caixa():
    comand = f"SELECT max(`id`) FROM dados_fechamentos_caixa;"
    result = conexao.bd_fetchall(comand)[0][0]
    result = int(result) + 1
    return result

def retorna_id_dados_fechamento_caixa_entra_data_sql(data_sql):
    comand = f"SELECT `id` FROM dados_fechamentos_caixa WHERE `data_caixa` = '{data_sql}';"
    result = conexao.bd_fetchall(comand)[0][0]
    result = int(result)
    return result

def retorna_data_max_caixas_fechados():
    comand = "SELECT max(`data_caixa`) FROM dados_fechamentos_caixa WHERE `caixa_fechado` = 1"
    result = conexao.bd_fetchall(comand)[0][0]
    return result

def retorna_data_para_fechar_caixa():
    from datetime import datetime, timedelta
    from app.utilitarios.datas.retornos_partes_da_data import retorna_ano_data, retorna_dia_data, retorna_mes_data
    from app.utilitarios.datas.retornos_formatos_datas import entra_data_dt_retorna_data_sql

    delta_tempo = timedelta(days=1)

    data_max_sql = retorna_data_max_caixas_fechados()

    dia_ultimo_fechamento = retorna_dia_data(data_max_sql)
    mes_ultimo_fechamento = retorna_mes_data(data_max_sql)
    ano_ultimo_fechamento = retorna_ano_data(data_max_sql)

    data_ultimo_fechamento_dt = datetime(day=dia_ultimo_fechamento, month=mes_ultimo_fechamento, year=ano_ultimo_fechamento).date()
    data_para_fechamento_caixa_dt = data_ultimo_fechamento_dt + delta_tempo

    data_para_fechamento_caixa_sql = entra_data_dt_retorna_data_sql(data_para_fechamento_caixa_dt)

    return(data_para_fechamento_caixa_sql)

def retorna_data_min_caixas_fechados():
    from datetime import datetime, timedelta
    from app.utilitarios.datas.retornos_partes_da_data import retorna_ano_data, retorna_dia_data, retorna_mes_data
    from app.utilitarios.datas.retornos_formatos_datas import entra_data_dt_retorna_data_sql
        
    comand = "SELECT min(`data_caixa`) FROM dados_fechamentos_caixa WHERE `caixa_fechado` = 1"
    result = conexao.bd_fetchall(comand)[0][0]

    dia = retorna_dia_data(result)
    mes = retorna_mes_data(result)
    ano = retorna_ano_data(result)

    delta_time = timedelta(days=1)
    data_dt = datetime(day=dia, month=mes, year=ano).date()
    data_min_dt = data_dt + delta_time

    data_min_sql = entra_data_dt_retorna_data_sql(data_min_dt)

    return data_min_sql

def retorna_troco_caixa_final_dia_anteiror(data_sql):
    from datetime import datetime, timedelta
    from app.utilitarios.datas.retornos_partes_da_data import retorna_ano_data, retorna_dia_data, retorna_mes_data
    from app.utilitarios.datas.retornos_formatos_datas import entra_data_dt_retorna_data_sql

    dia = retorna_dia_data(data_sql)
    mes = retorna_mes_data(data_sql)
    ano = retorna_ano_data(data_sql)

    delta_tempo = timedelta(days=1)
    data_dt = datetime(day=dia, month=mes, year=ano)
    data_dt_anterior = data_dt - delta_tempo
    data_sql_anterior = entra_data_dt_retorna_data_sql(data_dt_anterior)

    command = f"SELECT `troco_final_cx`,`estoque_troco_cx` FROM dados_fechamentos_caixa WHERE `data_caixa` = '{data_sql_anterior}'"
    result = conexao.bd_fetchall(command)

    return [result[0][0], result[0][1]]

def retorna_lista_tuplas_id_despesas_caixa():

    command = "SELECT `id`,`despesa` FROM despesas ORDER BY `despesa`;"

    result = conexao.bd_fetchall(command)

    lista = []

    for item in result:
        tuple_temp = (item[0], item[1])
        lista.append(tuple_temp)

    return lista

def retorna_lista_tuplas_id_tipos_entradas_n_operadora():

    tabela = 'tipos_entradas_n_operadora_maq'

    command = f"SELECT `id`,`tipo_entrada` FROM {tabela} ORDER BY `tipo_entrada`;"
    result = conexao.bd_fetchall(command)

    lista = []

    for item in result:
        tuple_temp = (item[0], item[1])
        lista.append(tuple_temp)

    return lista

def retorna_lista_dict_id_despesas_caixa_pelo_caixa_id(caixa_id):

    command = f"SELECT `id`, `despesa_id`, `descricao_despesa`, `valor_despesa` FROM despesas_caixa WHERE `caixa_id`={caixa_id} ORDER BY `descricao_despesa`;"
    result = conexao.bd_fetchall(command)

    lista = []

    for item in result:
        dict_temp = {}
        dict_temp['id'] = item[0]
        dict_temp['despesa_id'] = item[1]
        dict_temp['descricao_despesa'] = item[2]
        dict_temp['valor_despesa'] = item[3]
        lista.append(dict_temp)

    return lista

def retorna_lista_dict_insercao_entradas_n_operadora_caixa_pelo_caixa_id(caixa_id):
    tabela = 'entradas_n_operadora_maq'
    command = f"SELECT id, valor, tipo_entrada_n_operadora_maq_id FROM {tabela} WHERE caixa_id = {caixa_id}"
    result = conexao.bd_fetchall(command)

    lista = []

    for item in result:
        dict_temp = {}
        dict_temp['id'] = item[0]
        dict_temp['valor'] = item[1]
        dict_temp['id_tipo_entrada'] = item[2]
        dict_temp['tipo_entrada'] = retorna_tipo_entrada(item[2])
        lista.append(dict_temp)

    return lista

def retorna_tipo_entrada(id_entrada):

    tabela = 'tipos_entradas_n_operadora_maq'

    command = f"SELECT tipo_entrada FROM {tabela} WHERE id = {id_entrada};"
    result = conexao.bd_fetchall(command)

    return result[0][0]

def retorna_lista_dict_trocas_devolucoes_caixa_pelo_caixa_id(caixa_id):

    tabela = 'trocas_devolucoes_dia'

    command = f"SELECT `id`, `codigo_produto`, `tipo_ent_ou_sai`, `valor`, `entrada_ou_saida`, `relevancia_caixa` FROM {tabela} WHERE `caixa_id`={caixa_id};"
    result = conexao.bd_fetchall(command)

    lista = []

    for item in result:
        dict_temp = {}
        dict_temp['id'] = item[0]
        dict_temp['codigo_produto'] = item[1]
        dict_temp['id_forma'] = item[2]
        
        if int(item[2]) == 1:
            dict_temp['forma'] = 'Produto'

        if int(item[2]) == 2:
            dict_temp['forma'] = 'Dinheiro'

        if int(item[2]) == 3:
            dict_temp['forma'] = 'Débito'

        if int(item[2]) == 4:
            dict_temp['forma'] = 'Crédito'

        dict_temp['valor'] = item[3]
        dict_temp['entrada_saida'] = item[4]
        dict_temp['relevancia_caixa'] = item[5]

        lista.append(dict_temp)

    return lista

def retorna_lista_dict_observacoes_caixa_pelo_caixa_id(caixa_id):

    tabela = 'observacoes_caixa'

    command = f"SELECT `id`, `observacao_caixa` FROM {tabela} WHERE `caixa_id` = {caixa_id};"
    result = conexao.bd_fetchall(command)

    lista = []

    for item in result:
        dict_temp = {}
        dict_temp['id'] = item[0]
        dict_temp['observacao_caixa'] = item[1]
        lista.append(dict_temp)

    return lista

def inserir_despesa_caixa(descricao_despesa, valor_despesa, despesa_id, caixa_id, usuario_id):

    tabela = 'despesas_caixa'

    command = f"INSERT INTO {tabela} (descricao_despesa, valor_despesa, despesa_id, caixa_id, usuario_id) VALUES ('{descricao_despesa}', {valor_despesa}, {despesa_id}, {caixa_id}, {usuario_id})"

    try:
        conexao.bd_commit(command)
        return True
    except:
        return False

def inserir_observacao_caixa(observacao_caixa:str, caixa_id:int, usuario_id:int):
    tabela = 'observacoes_caixa'
    command = f"INSERT INTO {tabela} (`observacao_caixa`, `caixa_id`, `usuario_id`) VALUES ('{observacao_caixa}',{caixa_id},{usuario_id});"

    try:
        conexao.bd_commit(command)
        return True
    except:
        return False
    
def inserir_troca_devolucao(caixa_id:int, codigo_produto:str, tipo_ent_ou_sai:str, valor:float, entrada_ou_saida:str, relevancia:int, usuario_id:int) -> bool:
    
    tabela = 'trocas_devolucoes_dia'
    command = f"INSERT INTO {tabela} (`caixa_id`, `codigo_produto`, `tipo_ent_ou_sai`, `valor`, `entrada_ou_saida`, `relevancia_caixa`, `usuario_id`) VALUES ({caixa_id},'{codigo_produto}',{tipo_ent_ou_sai},{valor},'{entrada_ou_saida}','{relevancia}','{usuario_id}');"
    
    try:
        conexao.bd_commit(command)
        return True
    except:
        return False

def retorna_lista_despesas_caixa(caixa_id):
    command = f"SELECT `id`,`descricao_despesa`,`valor_despesa` FROM despesas_caixa WHERE `caixa_id`='{caixa_id}';"
    result = conexao.bd_fetchall(command)

    lista=[]
    valor_total_despesas = 0

    for item in result:
        dict_temp = {}
        dict_temp['id'] = item[0]
        dict_temp['descricao'] = item[1]
        dict_temp['valor'] = item[2]
        valor_total_despesas += item[2]
        lista.append(dict_temp)

    return [lista,valor_total_despesas]

def deletar_troca_devolucao_caixa(id_troca_devolucao):
    tabela = 'trocas_devolucoes_dia'
    command = f"DELETE FROM {tabela} WHERE id = {id_troca_devolucao};"

    try:
        conexao.bd_commit(command)
        return True
    except:
        return False

def deletar_observacao_caixa(id_observacao_caixa):
    tabela = 'observacoes_caixa'
    command = f"DELETE FROM {tabela} WHERE id = {id_observacao_caixa};"

    try:
        conexao.bd_commit(command)
        return True
    except:
        return False

def deletar_despesa_caixa(id_despesa_caixa):
    tabela = 'despesas_caixa'
    command = f"DELETE FROM {tabela} WHERE id = {id_despesa_caixa};"

    try:
        conexao.bd_commit(command)
        return True
    except:
        return False

def leitura_arquivo_caixa_fechado(caixa_id):

    command = f"SELECT `resultado_final_cx`,`troco_final_cx`,`estoque_troco_cx`,`vendas_total`,`vendas_dinheiro_dia`,`vendas_pix_direto_cnpj`,`vendas_operadoras_maq_cartao`,`vendas_pix_direto_cpf` FROM dados_fechamentos_caixa WHERE `id` = {caixa_id};"
    result = conexao.bd_fetchall(command)
    dict_temp = {}
    dict_temp['resultado_final_cx'] = result[0][0]
    dict_temp['troco_final_cx'] = result[0][1]
    dict_temp['estoque_troco_cx'] = result[0][2]
    dict_temp['vendas_total'] = result[0][3]
    dict_temp['vendas_dinheiro_dia'] = result[0][4]
    dict_temp['vendas_pix_direto_cnpj'] = result[0][5]
    dict_temp['vendas_operadoras_maq_cartao'] = result[0][6]
    dict_temp['vendas_pix_direto_cpf'] = result[0][7]

    return dict_temp

def inserir_fechamento_caixa_definitivo(data_caixa:str, caixa_id:int, usuario_id:int, resultado_final_cx:float, troco_final_cx:float, estoque_troco_cx:float, vendas_total:float, vendas_dinheiro_dia:float, vendas_pix_direto_cnpj:float, vendas_pix_direto_cpf:float, vendas_operadoras_maq_cartao:float, result_trocas_devs_dinheiro:float, result_trocas_devs_debito:float, result_trocas_devs_credito:float, result_trocas_devs_produtos:float, dia_caixa_fechado:int) -> bool:
    from datetime import datetime
    from app.utilitarios.datas.retornos_formatos_datas import entra_data_dt_retorna_data_sql

    data_agora = datetime.now()
    data_agora_dt = data_agora.date()

    data_sql = entra_data_dt_retorna_data_sql(data_agora_dt)
    hora = data_agora.hour
    minutos = data_agora.minute    

    tabela = 'dados_fechamentos_caixa'
    command = f"UPDATE {tabela} SET data_caixa = '{data_caixa}', data_fechamento='{data_sql}', hora={hora}, minutos={minutos}, caixa_fechado = 1, read_app_parent = 0, usuario_id = {usuario_id}, resultado_final_cx = {round(resultado_final_cx,2)}, troco_final_cx={troco_final_cx}, estoque_troco_cx={estoque_troco_cx}, vendas_total={vendas_total}, vendas_dinheiro_dia={vendas_dinheiro_dia}, vendas_pix_direto_cnpj={vendas_pix_direto_cnpj}, vendas_pix_direto_cpf={vendas_pix_direto_cpf}, vendas_operadoras_maq_cartao={vendas_operadoras_maq_cartao}, result_trocas_devs_dinheiro={result_trocas_devs_dinheiro}, result_trocas_devs_debito={result_trocas_devs_debito}, result_trocas_devs_credito={result_trocas_devs_credito}, result_trocas_devs_produtos={result_trocas_devs_produtos}, dia_loja_fechada={dia_caixa_fechado} WHERE id = {caixa_id};"
    
    try:
        conexao.bd_commit(command)
        return True
    except:
        print(command)
        return False

def inserir_fechamento_caixa_parcial(caixa_id:int, usuario_id:int, resultado_final_cx:float, troco_final_cx:float, estoque_troco_cx:float, vendas_total:float, vendas_dinheiro_dia:float, vendas_pix_direto_cpf:float, vendas_pix_direto_cnpj:float, vendas_operadoras_maq_cartao:float, result_trocas_devs_dinheiro:float, result_trocas_devs_debito:float, result_trocas_devs_credito:float, result_trocas_devs_produtos:float) -> bool:
    from datetime import datetime
    from app.utilitarios.datas.retornos_formatos_datas import entra_data_dt_retorna_data_sql

    data_agora = datetime.now()
    data_agora_dt = data_agora.date()

    data_sql = entra_data_dt_retorna_data_sql(data_agora_dt)
    hora = data_agora.hour
    minutos = data_agora.minute

    tabela = 'fechamentos_parciais_caixa'

    command = f"""INSERT INTO {tabela} 
    (`caixa_id`,`data`,`hora`, `minutos`, `usuario_id`, `read_app_parent`, 
    `resultado_final_cx`, `troco_final_cx`, `estoque_troco_cx`, `vendas_total`,
    `vendas_dinheiro_dia`, `vendas_pix_direto_cnpj`, `vendas_pix_direto_cpf`,
    `vendas_operadoras_maq_cartao`, `result_trocas_devs_dinheiro`,
    `result_trocas_devs_debito`, `result_trocas_devs_credito`,
    `result_trocas_devs_produtos`) VALUES
    ({caixa_id}, '{data_sql}', {hora}, {minutos}, {usuario_id},                 0,
     {resultado_final_cx}, {troco_final_cx}, {estoque_troco_cx}, {vendas_total},
     {vendas_dinheiro_dia}, {vendas_pix_direto_cnpj}, {vendas_pix_direto_cpf},
     {vendas_operadoras_maq_cartao}, {result_trocas_devs_dinheiro},
     {result_trocas_devs_debito}, {result_trocas_devs_credito}, 
     {result_trocas_devs_produtos})"""

    try:
        conexao.bd_commit(command)
        return True
    except:
        print('deu ruim fechamento parcial caixa')
        print(command)
        return False

def return_dict_fechamentos_parciais_cx(caixa_id):

    tabela = 'fechamentos_parciais_caixa'

    command = f"SELECT id, data, hora, minutos, usuario_id, resultado_final_cx FROM {tabela} WHERE caixa_id = {caixa_id} ORDER BY hora,minutos;"
    result = conexao.bd_fetchall(command)

    if len(result) == 0:
        return 0

    lista = []

    for item in result:
        dict_temp = {}
        dict_temp['id'] = item[0]
        dict_temp['data'] = item[1]
        dict_temp['hora'] = item[2]
        dict_temp['minutos'] = item[3]
        dict_temp['usuario'] = entra_code_user_return_name_user(item[4])
        dict_temp['resultado_cx'] = item[5]
        lista.append(dict_temp)

    return lista

def inserir_entrada_n_operadora_maq(caixa_id:int, usuario_id:int, valor:float, tipo_entrada_n_operadora_maq:int):

    tabela = 'entradas_n_operadora_maq'
    command = f"INSERT INTO {tabela} (caixa_id, usuario_id, valor, tipo_entrada_n_operadora_maq_id) VALUES ({caixa_id}, {usuario_id}, {valor}, {tipo_entrada_n_operadora_maq});"
    try:
        conexao.bd_commit(command)
        return True
    except:
        print(f'erro na inserção dos dados em {tabela}')
        return False

def deletar_entrada_n_operadora_maq(id_entrada):
    tabela = 'entradas_n_operadora_maq'
    command = f"DELETE FROM {tabela} WHERE id = {id_entrada};"
    try:
        conexao.bd_commit(command)
        return True
    except:
        print(f'erro na deleção dos dados em {tabela}')
        return False

