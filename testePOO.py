class Escola:
    def __init__(self, aluno, nota1, nota2, faltas):
        self.aluno = aluno
        self.nota1 = nota1
        self.nota2 = nota2
        self.__faltas = faltas
        self.media = (self.nota1 + self.nota2) / 2

    def CalcularMedia(self):
        print('a media do aluno {} eh {}'.format(self.aluno, self.media))

    def VerificarSituacao(self):
        if self.__faltas > 70:
            print('aluno reprovado')
        else:
            if self.media < 7:
                print('aluno reprovado')
            else:
                print('aluno aprovado')


aluno1 = Escola('adib', 7, 6, 71)

aluno1.CalcularMedia()
#aluno1.VerificarSituacao()

aluno1.faltas = 69
aluno1.VerificarSituacao()