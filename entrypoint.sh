#!/bin/sh
chmod +x entrypoint.sh

echo "Criando Tabelas..."
python3 manage.py makemigrations --noinput

echo "Aplicando migrações..."
python3 manage.py migrate --noinput

echo "Coletando arquivos estáticos..."
python3 manage.py collectstatic --noinput

echo "Iniciando o servidor..."
exec gunicorn --bind 0.0.0.0:8080 drf_quirons.wsgi:application
