# Por padrão a aws retorna as informações:
# event -> vem com várias informações como:
#   requisições do usuário
#   bady 
#   e outras mais
#context: -> vem informações para você colher dados da lambda
import json
def mensagens(event, context):
    return {
        "statusCode": 200,
        "body": "Ai chefe! O PDI tá indo! olha o serverless em ação....."
    }
    
def mensagem_parabens(event, context):
    resposta = list()
    resposta.append({"statusCode": 200,
        "body": [{"mensagem": "Olá Mundo Serverless"}]})
    return json.dumps(resposta, ensure_ascii=False)
    
    