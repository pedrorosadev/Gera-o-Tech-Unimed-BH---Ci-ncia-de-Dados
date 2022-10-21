from this import d


class Veiculo:
    def __init__(self, cor, placa, numero_rodas) -> None:
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        
    def ligar_motor(self):
        print('Ligando o motor')

class Carro(Veiculo):
    # def __init__(self) -> None:
    #     super().__init__()
    pass

class Motocicleta(Veiculo):
    # def __init__(self) -> None:
    #     super().__init__()
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado) -> None:
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carrega(self):
        print(f"{'Sim' if self.carregado else 'Não'}")

moto = Motocicleta('preta', 'abc-1234', 2)
moto.ligar_motor()

carro = Carro('vermelho', 'xde-0098', 4)
carro.ligar_motor()

caminhao = Caminhao('branco', 'pxo-2456', 8, False)
caminhao.ligar_motor()
caminhao.esta_carrega()
