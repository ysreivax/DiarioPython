import mysql.connector
from conexao import conexao

class Model:
    def __init__(self):
        self.db_connection = conexao() #Abrindo conexao com o banco
        self.db_connection = self.db_connection.conectar()#Metodo que faz a conexao com o DB
        self.con = self.db_connection.cursor() #Navegação no banco de dados; cursor é uma variavel da classe mysql.connector

    def inserir(self, nome, telefone, email, dataDeNascimento, pagina):
        try:
            sql = "insert into pessoa(codigo, nome, telefone, email, dataDeNascimento, pagina) values('', '{}', '{}', '{}', '{}', '{}')".format(
                nome, telefone, email, dataDeNascimento, pagina)
            self.con.execute(sql)  # Prepara o dado para ser inserido
            self.db_connection.commit()  # Insere o dado no banco
            return "{} linha(s) afetada(s)".format(self.con.rowcount)  # Rowcount é uma variavel da classe mysql
        except Exception as erro:
            return erro

    def selecionar(self):
        try:
            sql = "select * from pessoa"
            self.con.execute(sql)  # Devolve os dados salvos
            msg = ""
            for (codigo, nome, telefone, email, dataDeNascimento, pagina) in self.con:
                msg += "\nCódigo: {}, Nome: {}, Telefone: {}, email: {}, Data de Nascimento: {}, Pagina: {}".format(codigo, nome, telefone, email, dataDeNascimento, pagina)
            return msg
        except Exception as erro:
            return erro

    def atualizar(self, campo, novoDado, cod):
        try:
            sql = "update pessoa set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha(s) atualizada(s)!".format(self.con.rowcount)
        except Exception as erro:
            return erro

