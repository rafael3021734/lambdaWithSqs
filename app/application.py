import json
from model import Contrato, Data, Parcela


# import requests

def lambda_handler(event, context):
    # TODO implement
    print(event)

    for record in event.get('Records'):
        print(event)
        body = json.loads(record.get('body'))
        contrato = body.get("contrato")
        parcela = body.get("parcela")
        print(f' body: {body}')
        print(f' Contrato: {contrato}')
        lista = []
        listaPar= []

        for cont in contrato:
            objectContrato = Contrato.Contrato(
            NumContrato= cont['NumContrato'],
            Serie=cont['Serie'],
            id=cont['id'],
            dataContratacao=(cont['dataContratacao'])
            )
            lista.append(objectContrato.__dict__)
        #listaPar.append(parcela)
        #parce = parcelaLista(parcela)
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
        #print(f'parcela:{listaPar}')
        print(f'parcela:{parce}')
        print(f'Objeto: {objectContrato.__dict__}')
        print(f'data:{data.__dict__}')
        #print(f'Objeto: {objectContrato.__dict__}')

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