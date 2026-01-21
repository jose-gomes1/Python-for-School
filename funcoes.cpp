class Pessoa:

    nome = "" # public
    idade = 0

    _morada = "" # protected

    __telefone_ = 0 # private

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def _getNome(self): # protected
        return self.nome
    
    def __getTelefone_(self): # private
        return self.__telefone
    
p1 = Pessoa("João", 30)
print(p1._getNome())
# print(p1.__getTelefone_())

class Aluno(Pessoa):
    curso = ""
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso
