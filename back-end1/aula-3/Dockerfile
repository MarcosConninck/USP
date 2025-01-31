# Use a imagem Python 3.12
FROM python:3.12

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Instalando dependências do projeto
RUN pip install requests
RUN pip install types-requests

# Copie todos os seus arquivos Python para o contêiner
COPY . src/app