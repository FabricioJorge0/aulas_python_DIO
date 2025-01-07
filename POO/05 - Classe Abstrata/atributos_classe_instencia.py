class Estudante:
    escola = 'DIO'

    def __init__(self, nome, matricula):
        self.nome = nome 
        self.matricula = matricula

    def __str__(self):
        return f'{self.nome} - {self.matricula} - {self.escola}'
    

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
    


aluno1 = Estudante('Guilherme', 1)
aluno2 = Estudante('Fabricio', 13)

mostrar_valores(aluno1, aluno2)


aluno3 = Estudante('Ze', 3)

Estudante.escola = 'Python'
mostrar_valores(aluno1, aluno2, aluno3)
