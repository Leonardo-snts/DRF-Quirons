# Usa uma imagem oficial do Python como base
FROM python:3.11

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos de dependências para o container
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante da aplicação para o container
COPY . .

# Define a variável de ambiente para o Django rodar no Cloud Run
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=drf_quirons.settings

# Expõe a porta usada pelo Django (necessário para Cloud Run)
EXPOSE 8080

# Comando para rodar a aplicação
CMD ["sh", "/app/entrypoint.sh"]
