def tratamento_valor(valor):

    from decimal import Decimal

    if valor == None:
        valor_decimal = Decimal(0)
        return valor_decimal
    
    if len(valor) == 0:
        valor_decimal = Decimal(0)
        return valor_decimal

    valor = valor.replace(',','.')
    valor_decimal = Decimal(valor)

    return valor_decimal

def tratamento_booleano(valor_bool):

    valor_bool_retorno = valor_bool

    if valor_bool == '' or valor_bool == '0' or valor_bool == None:
        valor_bool_retorno = 0

    if valor_bool == '1' or valor_bool == 'on':
        valor_bool_retorno = 1

    return valor_bool_retorno