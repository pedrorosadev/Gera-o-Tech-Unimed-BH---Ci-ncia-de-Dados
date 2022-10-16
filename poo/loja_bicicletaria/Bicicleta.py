

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18, marcha=1):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro
        self.marcha = marcha

    def buzinar(self):
        print('Plim plim !!!')

    def parar(self):
        print('Parando a bicicleta...')
        print('Bicicleta parada...')

    def correr(self):
        print('Acelerando...')
        print('Vruuuum...')

    def trocar_marcha(self, numero_marcha):
        print('Trocando Marcha')
        _self = self

        def _trocar_marcha():
            if numero_marcha > _self.marcha:
                print('Marcha Trocada...')
            else:
                print('Não foi possível trocar de marcha...')

    #def __str__(self) -> str:
    #    return f'Bicicleta: cor: {self.cor}, modelo: {self.modelo}, ano: {self.ano}, valor: {self.valor}'

    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {", ".join([f"{chave}:{valor}" for chave, valor in self.__dict__.items()])}'


'''
b1 = Bicicleta(cor='vermelha', modelo='caloi', ano='ano', valor='600')
b1.buzinar()
b1.correr()
b1.parar()
print(f'\n\nModelo: {b1.modelo} \nCor:{b1.cor}\nAno: {b1.ano}\nValor: R$ {b1.valor}\n')
'''

b2 = Bicicleta('verde', 'monark', 2000, 189)
print(b2)