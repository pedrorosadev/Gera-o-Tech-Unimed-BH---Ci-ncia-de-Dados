class Animal:
    def __init__(self, numero_patas) -> None:
        self.numero_patas = numero_patas

    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {", ".join([f"{chave}:{valor}" for chave, valor in self.__dict__.items()])}'


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw) -> None:
        self.cor_pelo = cor_pelo

        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw) -> None:
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Cachorro(Mamifero):
    def __init__(self, numero_patas, cor_pelo) -> None:
        super().__init__(numero_patas, cor_pelo)      

class Gato(Mamifero):
    def __init__(self, numero_patas, cor_pelo) -> None:
        super().__init__(numero_patas, cor_pelo)      

class Leao(Mamifero):
    def __init__(self, numero_patas, cor_pelo) -> None:
        super().__init__(numero_patas, cor_pelo)      

class Ornitorrinco(Mamifero, Ave):
    pass

# gato = Gato(4, 'preto')
# print(gato)

ornitorrinco = Ornitorrinco(numero_patas=2, cor_pelo='branco', cor_bico='preto')
print(ornitorrinco)