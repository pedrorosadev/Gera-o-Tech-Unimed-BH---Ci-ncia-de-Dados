class Cachorro:
    def __init__(self, nome, cor, acordado=True) -> None:
        print('Inicializando a classe...')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self) -> None:
        print('Removendo a instância da classe...')
        
    def latir(self):
        print('Au au au!')

c = Cachorro('Alice', 'Preto e Branco')
c.latir()