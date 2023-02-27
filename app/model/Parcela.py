

class Parcela:

    def __init__(self, NumContrato, Parcela, qtdParcela):
        self.NumContrato = NumContrato
        self.Parcela = Parcela
        self.qtdParcela = qtdParcela

    def parcelaLista(parcela):
        listaPar = []
        for par in parcela:
            parcela = Parcela(
                NumContrato=par['NumContrato'],
                Parcela=par['Parcela'],
                qtdParcela=par['qtdParcela']
            )
            listaPar.append(parcela.__dict__)
        return listaPar