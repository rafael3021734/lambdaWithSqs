from testeSendMessage2 import send_json, return_all, create_queue


# 1) Criar uma fila no SQS
# 2) Criar uma tabela no DynamoDB

create_queue()

# 3) Enviar mensagens para fila SQS
send_json({
    'first_number' : 14,
    'second_number' : 20
})
send_json({
    'first_number' : 15,
    'second_number' : 20
})

# 4) Ler as mensagens da fila SQS
result = return_all()
for r in result:
    # 5) Gravar os dados no DynamoDB
    send_data(r)

# 6) Ler os dados do DynamoDB
res_dynamo = return_data()
for r in res_dynamo:
    print(r)