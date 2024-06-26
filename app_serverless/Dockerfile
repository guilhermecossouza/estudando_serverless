FROM python:3.10-slim

#COMANDOS GLOBAIS   
RUN apt-get update
RUN apt-get install -y curl
RUN rm -rf /var/lib/apt/lists/*
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g serverless@3
RUN apt-get update

WORKDIR /app_serverless

COPY . .

#plugin para rodar o serverless em modo offiline
RUN serverless plugin install -n serverless-offline

RUN pip install -r requirements.txt

#EXPOSE 3000

CMD [ "serverless", "offline", "--host", "0.0.0.0" ]



