import sqlite3

class Conexao:

    def __init__(self):
        from pathlib import Path        
        pasta_banco_de_dados = 'database_app'        
        file_banco = Path(pasta_banco_de_dados).joinpath('app_cashier.db')
        self.banco_dados = sqlite3.connect(file_banco)

    def bd_fetchall(self, command):
        cursor = self.banco_dados.cursor()
        try:
            cursor.execute(command)
            dados = cursor.fetchall()
            return dados
        except sqlite3.Error as e:
            print(f"Erro SQLite: -> {e}")            
            print(f'erro em: {command}')
            return 0

    def bd_commit(self, command):
        cursor = self.banco_dados.cursor()
        
        try:
            cursor.execute(command)
            self.banco_dados.commit()
            condicao = True            
        except sqlite3.Error as e:
            print(f"Erro SQLite: -> {e}")
            print(f"erro em \n{command}")
            condicao = False

        return condicao
    
    def desconectar(self):
        self.banco_dados.close()

