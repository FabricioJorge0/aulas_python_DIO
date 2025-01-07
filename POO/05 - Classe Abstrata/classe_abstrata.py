from abc import ABC, abstractmethod

class ControleRomoto(ABC):
    

    @abstractmethod
    def ligar(self):
        pass


    @abstractmethod
    def desligar(self):
        pass


class ControleTv(ControleRomoto):
    def ligar(self):
        print('Ligando TV')
    
    def desligar(self):
        print('desligando TV')


class ControleArCondicionado(ControleRomoto):
    def ligar(self):
        print('Ligando ar condicionado')
    
    def desligar(self):
        print('Desligando arcondicionado')



controle = ControleTv()

controle.ligar()
controle.desligar()

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()