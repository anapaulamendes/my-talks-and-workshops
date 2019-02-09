class Animal:
    def __init__(self, nome, som):
        self.nome = nome
        self.som = som

gato = Animal("gato", "miau")
print(gato.nome, gato.som)

cachorro = Animal("cachorro", "auau")
print(cachorro.nome, cachorro.som)

galinha = Animal("galinha", "cócó")
print(galinha.nome, galinha.som)
