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
