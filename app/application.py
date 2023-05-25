import json
from model import Contrato, Data, Parcela


# import requests

def lambda_handler(event, context):
    # TODO implement
    print(event)

    for record in event.get('Records'):
        print(event)
        body = json.loads(record.get('body'))
        if 'md5' in body:
            md5_value = body['md5']
            print(f'body: 10, md5: {md5_value}')
        else:
            contrato = body.get("contrato")
            parcela = body.get("parcela")
            print(f' body: {body}')
            print(f' Contrato: {contrato}')
            lista = []
            listaPar = []

            my_list = [1, 2, 3, 4, 5]
            double_list = map(Contrato.Contrato.double, my_list)
            print(list(double_list))
     #       mapobjet = map(Contrato.Contrato.contractImpl, [("1", "1", "1", "1")])
     #       print(f' map: {list(mapobjet)}')

            for cont in contrato:
                objectContrato = Contrato.Contrato(
                    NumContrato=cont['NumContrato'],
                    Serie=cont['Serie'],
                    id=cont['id'],
                    dataContratacao=(cont['dataContratacao'])
                )
                lista.append(objectContrato.__dict__)
            # listaPar.append(parcela)
            # parce = parcelaLista(parcela)
            parce = Parcela.Parcela.parcelaLista(parcela)
            #    for par in parcela:
            #        parcela = Parcela.Parcela(
            #            NumContrato=par['NumContrato'],
            #            Parcela=par['Parcela'],
            #            qtdParcela=par['qtdParcela']
            #        )
            #        listaPar.append(parcela.__dict__)

            data = Data.Data(lista, listaPar)
            data = Data.Data(lista, parce)
            print(f'lista:{lista}')
            # print(f'parcela:{listaPar}')
            print(f'parcela:{parce}')
            print(f'Objeto: {objectContrato.__dict__}')
            print(f'data:{data.__dict__}')
            md = "123"
            #md5 = "md5": md}
            md5 = json.dumps(md)
            json_body = json.dumps(body)
            #json_body = json.dumps(md5)
            #bodyjson = { body, md5}
            print(f'body:{{{json_body},"md5":{md5}}}')

            body = {"key1": "value1", "key2": "value2"}

            # Converter o objeto 'body' em uma string JSON formatada
            json_body = json.dumps(body, indent=4)

            # Exibir a string JSON formatada
            print(f'body: {json_body}, {md5}')

            # print(f'Objeto: {objectContrato.__dict__}')

            # id_person = body.get('id')
            # name = body.get('name')
            # print(f'Name: {name}, ID:{id_person}')
            # print(f'teste:{body}')
    return {
        'statusCode': 200,
        # 'body': json.dumps('Hello from Lambda!')
    }


def parcelaLista(parcela):
    listaPar = []
    for par in parcela:
        parcela = Parcela.Parcela(
            NumContrato=par['NumContrato'],
            Parcela=par['Parcela'],
            qtdParcela=par['qtdParcela']
        )
        listaPar.append(parcela.__dict__)
    return listaPar
