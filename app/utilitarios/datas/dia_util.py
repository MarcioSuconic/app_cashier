class Retorna_Proximo_Dia_Util:

    def __init__(self, data_sql, dias_a_mais):
        self.data_sql = data_sql
        self.dias_a_mais = dias_a_mais
        self.__segue_o_fluxo()

    def __segue_o_fluxo(self):
        self.__muda_data_sql_para_datetime()
        self.__cria_delta_dt()
        self.__data_mais_dias_a_mais()
        self.__verifica_dia_util()
        #self.__verifica_feriado()
        self.__transaforma_dt_para_sql()

    def __muda_data_sql_para_datetime(self):
        from datetime import date
        from utilitarios.datas.retornos_formatos_datas import entra_data_dt_retorna_data_sql

        if str(type(self.data_sql)) == "<class 'datetime.date'>":
            self.data_sql = entra_data_dt_retorna_data_sql(self.data_sql)

        dia = self.data_sql[8:10]
        mes = self.data_sql[5:7]
        ano = self.data_sql[0:4]
        self.data_dt = date(day=int(dia), month=int(mes), year=int(ano))

    def __cria_delta_dt(self):
        from datetime import timedelta
        self.delta_prazo = timedelta(days=int(self.dias_a_mais))

    def __data_mais_dias_a_mais(self):
        self.prazo_sem_analise_dt = self.data_dt + self.delta_prazo

    def __verifica_dia_util(self):
        from datetime import timedelta

        delta_base_dt = timedelta(days=1)

        self.data_final_dt = self.prazo_sem_analise_dt

        while self.data_final_dt.weekday() >= 5:
            self.data_final_dt = self.data_final_dt + delta_base_dt

    def __transaforma_dt_para_sql(self):
        self.data_final_sql = str(self.data_final_dt)

    def __verifica_feriado(self):
        
        from datetime import datetime, timedelta
        lista_feriados = retorna_lista_feriados()

        eh_feriado = True

        while eh_feriado == True:

            for item in lista_feriados:
                dia = item[0]
                mes = item[1]

                if (self.data_final_dt.day == dia and self.data_final_dt.month == mes):
                    eh_feriado = True
                    self.data_final_dt = self.data_final_dt + timedelta(days=1)
                    break
                
            eh_feriado = False

    def retorna_a_data_final(self):
        return self.data_final_sql

def retorna_lista_feriados():
    lista_feriados =[(1,1),(25,1),(18,4),(21,4),(1,5),(19,6),(9,7),(7,9),(12,10),(2,11),(15,11),(20,11),(25,12)]
    return lista_feriados
