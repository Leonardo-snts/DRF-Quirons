import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
# Informações de conexão
host =os.getenv('DB_HOST')
database =os.getenv('DB_NAME')
user =os.getenv('DB_USER')
password =os.getenv('DB_PASSWORD')
port =os.getenv('DB_PORT')

try:
    # Conexão
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port
    )
    print("Conexão bem-sucedida!")
    conn.close()

except Exception as e:
    print(f"Erro ao conectar: {e}")
