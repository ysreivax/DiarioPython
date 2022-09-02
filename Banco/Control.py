from Model import Model

class Control:
    def __init__(self):
        self.opcao = -1
        self.modelo = Model()

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def Menu(self):
        print("\n\n BEM VINDO(A) AO SEU DIARIO VIRTUAL (: \n\n " +
              "\n0  Sair"                                        +
              "\n01 Cadastrar"                                   +
              "\n02 Escrever No Diario"                          +
              "\n03 Consultar Páginas"                           +
              "\n04 Atualizar Dados"                             +
              "\n05 Atualizar Nome"                              +
              "\n06 Atualizar Telefone"                          +
              "\n07 Atualizar email"                             +
              "\n08 Atualizar Data de nascimento"                +
              "\n09 Excluir Páginas")
        self.setOpcao(int(input()))

    def operacoes(self):
        while self.getOpcao() != 0:
            self.Menu()
            if self.getOpcao() == 0:
                print("Obrigado!")
            elif self.getOpcao() == 1:
                self.cadastrar()
            elif self.getOpcao() == 2:
                print(self.modelo.selecionar())
            elif self.getOpcao() == 3:
                print(self.modelo.selecionar.EscreverDiario)
            elif self.getOpcao() == 5:
                pass
            elif self.getOpcao() == 5:
                self.atualizarNome()
            elif self.getOpcao() == 6:
                self.atualizarEmail()
            elif self.getOpcao() == 7:
                self.atualizarTelefone()
            elif self.getOpcao() == 8:
                self.atualizarData()
            elif self.getOpcao() == 9:
                self.excluir(self.modelo.selecionar.EscreverDiario)
            else:
                print("Opção inválida! Tente novamente.")

    def cadastrar(self):
        print("Informe o seu nome:")
        nome = input()
        print("Informe o seu telefone:")
        telefone = input()
        print("Informe o seu email:")
        email = input()
        print("Informe o seu data de nascimento:")
        dataDeNascimento = input()
        print(self.modelo.inserir(nome, telefone, email, self.transformarData(dataDeNascimento)))

    def transformarData(self, texto):
        separado = texto.split('/')
        dia = separado[0]
        mes = separado[1]
        ano = separado[2]
        return "{}-{}-{}".format(ano, mes, dia)

    def atualizarNome(self):
        print("Informe o código do dado que será atualizado:")
        codigo = int(input())
        print("Informe o novo nome:")
        name = input()
        print(self.modelo.atualizar("nome", name, codigo))

    def atualizarTelefone(self):
        print("Informe o código do dado que será atualizado:")
        codigo = int(input())
        print("Informe o novo telefone:")
        tel = input()
        print(self.modelo.atualizar("telefone", tel, codigo))

    def atualizarEmail(self):
        print("Informe o código do dado que será atualizado:")
        codigo = int(input())
        print("Informe o novo email:")
        end = input()
        print(self.modelo.atualizar("email", end, codigo))

    def atualizarData(self):
        print("Informe o código do dado que será atualizado:")
        codigo = int(input())
        print("Informe  a nova data de nascimento:")
        data = self.transformarData(input())
        print(self.modelo.atualizar("dataDeNascimento", data, codigo))

    def EscreverDiario(self):
        for i in range(3):
            print("Página N° {} :".format(i + 1))
            pagina = int(input)
            print(self.modelo.inserir(pagina))

