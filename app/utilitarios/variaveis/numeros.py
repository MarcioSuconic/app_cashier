def entra_str_sai_float(valor_str) -> float:

    valor_str = str(valor_str)
    valor_str = valor_str.replace(',','.')
    lista_nova = []
    tamanho_valor_str = len(valor_str)

    for i in range(0,tamanho_valor_str):
        if valor_str[i].isdigit() or valor_str[i] == '.':
            lista_nova.append(valor_str[i])

    tamanho_lista_nova = len(lista_nova)

    valor_novo = ''

    for i in range(0,tamanho_lista_nova):
        valor_novo += lista_nova[i]

    valor_float = round(float(valor_novo),2)
 
    return valor_float

def entra_float_sai_valor_em_real(valor_float: float) -> str:
    valor_float = float(valor_float)
    valor_float = round(valor_float,2)   

    valor_str = str(valor_float).replace('.',',')

    lista = valor_str.split(',')

    if len(lista[1]) == 1:
        valor_str += '0'

    if len(lista[1]) == 0:
        valor_str += '00'
    
    valor_str = 'R$ ' + valor_str

    return valor_str
