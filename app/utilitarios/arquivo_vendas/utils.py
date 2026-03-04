import os

def entra_data_dt_retorna_data_sql(data_dt):
    from datetime import datetime

    if data_dt == '':
        return ''

    dia_data = str(data_dt.day)
    mes_data = str(data_dt.month)
    ano_data = str(data_dt.year)

    dia_data = retorna_2_digitos(dia_data)
    mes_data = retorna_2_digitos(mes_data)

    return f"{ano_data}-{mes_data}-{dia_data}"

def entra_data_sql_retorna_normal(data_sql):
    ano = data_sql[0:4]
    mes = data_sql[5:7]
    dia = data_sql[8:10]
    return(f'{dia}/{mes}/{ano}')

def entra_data_dt_retorna_texto(data_dt):
    
    lista_meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

    dia = str(data_dt.day)
    mes = str(data_dt.month)
    ano = str(data_dt.year)

    indice_mes = int(mes) - 1
    mes_texto = lista_meses[indice_mes]

    dia = retorna_2_digitos(dia)
    mes = retorna_2_digitos(mes)

    data_texto = f'São Paulo, {dia} de {mes_texto} de {ano}.'

    return (data_texto)

def retorna_2_digitos(variavel):

    variavel = str(variavel)

    if len(variavel) == 1:
        variavel = '0' + variavel

    return variavel

def basic_datas():
    dados = {}
    dados["criador"] = "Marcio Gonçalves Crancianinov Suconic"
    return dados

def return_path_base():
    from pathlib import Path

    caminho_base = os.getcwd()    
    return caminho_base

def return_read_path_file_sales(date_sql):

    from pathlib import Path
    
    dia = retorna_dia_data_str(date_sql)
    mes = retorna_mes_data_str(date_sql)
    ano = retorna_ano_data_str(date_sql)

    path_file = Path(return_path_base()).joinpath('arquivos_excel_sistema_euro').joinpath(f'{ano}').joinpath(f'{mes}').joinpath('vendas').joinpath(f'vendas_{dia}_{mes}_{ano}.xlsx')

    return path_file

def return_save_path_file_sales(date_sql):

    import os
    from pathlib import Path
    
    dia = retorna_dia_data_str(date_sql)
    mes = retorna_mes_data_str(date_sql)
    ano = retorna_ano_data_str(date_sql)
    
    base = os.getcwd()
    caminho = Path(base)/"databases_out"/"sales_x_products"/f"sales_{ano}_{mes}_{dia}.json"
    print(f'o caminho para gravar o JSON é: {caminho}')
    
    return caminho

def retorna_mes_data(data_sql):
    mes_data = data_sql[5:7]
    return int(mes_data)

def retorna_ano_data(data_sql):
    ano_data = data_sql[0:4]
    return int(ano_data)

def retorna_dia_data(data_sql):
    dia_data = data_sql[8:10]
    return int(dia_data)

def retorna_mes_data_str(data_sql):
    mes_data = data_sql[5:7]
    return str(mes_data)

def retorna_ano_data_str(data_sql):
    ano_data = data_sql[0:4]
    return str(ano_data)

def retorna_dia_data_str(data_sql):
    dia_data = data_sql[8:10]
    return str(dia_data)

def return_next_date_open_cashier():

    from datetime import datetime,timedelta

    delta_time = timedelta(days=1)
    date_last_closed_cashier = return_last_date_closed_cashier()
    day_closed = int(retorna_dia_data_str(date_last_closed_cashier))
    month_closed = int(retorna_mes_data_str(date_last_closed_cashier))
    year_closed = int(retorna_ano_data_str(date_last_closed_cashier))

    date_dt_closed_cashier = datetime(day=day_closed, month=month_closed, year= year_closed).date()
    next_date_open_cashier_dt = date_dt_closed_cashier + delta_time

    next_date_open_cashier_sql = entra_data_dt_retorna_data_sql(next_date_open_cashier_dt)

    return next_date_open_cashier_sql

def return_datas_closed_cashier(data_sql):

    import json
    from pathlib import Path

    base_path = return_path_base()

    day_consult = retorna_dia_data_str(data_sql)
    month_consult = retorna_mes_data_str(data_sql)
    year_consult = retorna_ano_data_str(data_sql)

    aditional_path = Path('databases_out').joinpath('closed_cashiers').joinpath(f'closed_cashier_{year_consult}_{month_consult}_{day_consult}.json')
    complete_path = Path(f'{base_path}').joinpath(f'{aditional_path}')

    with open(complete_path, 'r', encoding='utf-8') as file:
        datas = json.load(file)

    return (datas[data_sql])

