import psycopg2
import os
from dotenv import load_dotenv #carrega arq de variaveis
import time
import uuid

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a string de conexão do PostgreSQL do arquivo .env
CONN_POSTGRESQL = os.getenv('CONN_POSTGRESQL')

# Gerar um UUID dinamicamente &  Converte o UUID para string, se necessário
GUID = str(uuid.uuid4())
GUID = '556ac000-2084-4f10-80ef-df70ccfc0027'

def Exec_Chamada_Postgres(Nm_Objeto, uuid_param, ID_Tipo):
    try:
        # Estabeleça a conexão com o banco de dados
        conn = psycopg2.connect(CONN_POSTGRESQL)

        # Crie um cursor para executar consultas SQL
        cur = conn.cursor()
        
        if ID_Tipo == 1 : 
            # Execute a chamada do procedimento armazenado usando 'CALL' e passe o UUID como um parâmetro
            cur.execute(f'CALL {Nm_Objeto}(%s)', (uuid_param,))     
            conn.commit()

            print("Procedimento armazenado executado com sucesso.")
            
        if ID_Tipo == 2: 
            # Executar a função do PostgreSQL e passar o _ID_Guid como argumento   
            #cur.execute('SELECT * FROM "db_DxCorp_Servicos".spr_sel_log(%s)', (dynamic_uuid_str,))
            cur.execute(f'SELECT * FROM {Nm_Objeto}(%s)', (uuid_param,))  

            # Obter os resultados
            results = cur.fetchall()

            # Imprimir os resultados
            for row in results:
                print(row)
            
            print("Consulta executada com sucesso.")
            # Faça o commit das mudanças
        
        time.sleep(10)

    except Exception as e:
        print("Erro ao executar o procedimento armazenado:", e)

    finally:
        # Feche o cursor e a conexão@
        if cur:
            cur.close()
        if conn:
            conn.close()