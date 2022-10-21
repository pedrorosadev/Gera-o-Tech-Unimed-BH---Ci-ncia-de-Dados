from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print('Ligando a TV')
        print('Ligar !')

    def desligar(self):
        print('Desligando a TV...')
        print('Desligado !')

    @property
    def marca(self):
        return 'LG'

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando o Ar Condicionado...')
        print('Ligado !')

    def desligar(self):
        print('Desligando o Ar-Condicionado...')
        print('Desligado !')

    @property
    def marca(self):
        return 'Philco'


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle1 = ControleArCondicionado()
controle1.ligar()
controle1.desligar()
print(controle1.marca)