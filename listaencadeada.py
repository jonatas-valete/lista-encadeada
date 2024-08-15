from remover import remover


class Prontuario:
    def __init__(self, paciente, diagnostico, tratamento, proximo=None):
        self.paciente = paciente
        self.diagnostico = diagnostico
        self.tratamento = tratamento
        self.proximo = proximo

    def __repr__(self):
        return f'{self.paciente}'
              
class ListaEncadeadaProntuarios:
    def __init__(self):
        self.cabeca = None
    
    def adicionarProntuario(self, paciente, diagnostico, tratamento):
        """ Adiciona um prontuario na lista """
        novo_prontuario = Prontuario(paciente, diagnostico, tratamento, self.cabeca)
        self.cabeca = novo_prontuario

    def removerProntuario(self, paciente_nome:str):
        """ remover prontuario da lista """
        remover(self.cabeca, paciente_nome)
        
    def buscarProntuarios(self, nome_paciente):
        """ retorna um prontuario existente na lista """
        atual = self.cabeca
        while atual:
            if atual.paciente == nome_paciente:
                return atual
            atual = atual.proximo
        return None
        
    def quantidadeNo(self):
        """ contar quantidades de no na lista """
        contador = 0
        atual = self.cabeca
        while atual:
            contador+=1
            atual = atual.proximo
        return contador        
