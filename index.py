from dotenv import load_dotenv
import os
from Model.Metodos_psycopg2_postgres import Exec_Chamada_Postgres
import uuid

# Gerar um UUID dinamicamente & Converter o UUID para string, se necessário
GUID =  str(uuid.uuid4())
GUID = '556ac000-2084-4f10-80ef-df70ccfc0027'

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

if __name__ == "__main__":
    # Passe o nome do procedimento armazenado e o UUID como argumentos
    #ID_Tipo = 1 Procedure (insert, update ou delete) - ID_Tipo = 2 Function de seleção (Read)
    ID_tipo = 2

  # Defina o nome do objeto com base no tipo de operação
    if ID_tipo == 1:
        Nm_Objeto = '"db_DxCorp_Servicos".spr_taskmanager_0001'
    elif ID_tipo == 2:
        Nm_Objeto = '"db_DxCorp_Servicos".spr_sel_log'

    Exec_Chamada_Postgres(Nm_Objeto, GUID, ID_tipo)
