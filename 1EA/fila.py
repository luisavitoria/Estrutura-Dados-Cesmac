class AtendimentoSecretaria:
    def __init__(self):
        self.fila = []

    def estaVazia(self):
        return len(self.fila) == 0
    
    def tamanhoFila(self):
        print(f'A fila está com {len(self.fila)} estudante(s) aguardando atendimento. \n')

    def adicionarEstudante(self, estudante):
        print(f'Estudante {estudante} adicionado à fila. \n')
        self.fila.append(estudante)
    
    def removerEstudante(self):
        if self.estaVazia() == False:
            estudante = self.fila.pop(0)
            return estudante         

    def atenderEstudante(self):
        if self.estaVazia():
            print("Não há estudantes aguardando na fila. \n")
        else:
            estudante = self.removerEstudante()
            print(f"Atendendo o(a) estudante {estudante}. \n")
       

atendimento = AtendimentoSecretaria()

atendimento.adicionarEstudante("João")
atendimento.adicionarEstudante("Maria")
atendimento.adicionarEstudante("Paula")
atendimento.adicionarEstudante("Carlos")

atendimento.tamanhoFila()

atendimento.atenderEstudante()
atendimento.atenderEstudante()

atendimento.tamanhoFila()

atendimento.atenderEstudante()
atendimento.atenderEstudante()
atendimento.atenderEstudante()

atendimento.adicionarEstudante("José")

atendimento.atenderEstudante()

atendimento.tamanhoFila()





