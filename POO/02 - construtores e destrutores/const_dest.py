class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print('inicializando a classe')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def __del__(self):
        print('removendo a instancia da classe')
    
    def latir(self):
        print('auaua')

def criar_cachorro():
    c = Cachorro('Zeus', 'Branco', False)
    print(c.nome)
    
c = Cachorro('Thor', 'preto')
c.latir()
criar_cachorro()