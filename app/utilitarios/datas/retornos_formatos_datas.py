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

def return_dt_entry_sql(date_sql):

    from app.utilitarios.datas.retornos_partes_da_data import retorna_ano_data, retorna_dia_data, retorna_mes_data
    from datetime import datetime

    dia = retorna_dia_data(date_sql)
    mes = retorna_mes_data(date_sql)
    ano = retorna_ano_data(date_sql)

    data_dt = datetime(day=dia, month=mes, year=ano).date()

    return data_dt