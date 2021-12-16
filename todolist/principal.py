#importa o conector do mysql e o Error
from logging import error, info
import mysql.connector
from mysql.connector import Error

def criarBase():
    #Informar user e password referentes aos dados da máquina
    try:
        cnx = mysql.connector.connect(host='localhost', user='root', password='1234')
        cursor = cnx.cursor()
        cursor.execute("create database db_todo_list")
        print('Banco de dados criado com sucesso!')
    except Error as erro:
        print('Houve algum erro ao criar o banco de dados', erro)
    
    
def criarTabela():
    #Informar user e password referentes aos dados na máquina.
    try:
        cnx = mysql.connector.connect(host='localhost', user='root', password='1234', database='db_todo_list')
        cursor = cnx.cursor()
        cursor.execute("create table tarefas (id int primary key auto_increment, detalhes varchar(45) not null, dia varchar(10) not null, hora varchar(5) not null, local varchar(20))")
        print('Tabela criada com sucesso!')
    except Error as erro:
        print('Houve algum erro ao criar a tabela', erro)
    
#Criação da classe List
class List:
    #Cria parâmetros vazios.
    def __init__(self):
        self.id = None
        self.detalhes = None
        self.dia = None
        self.hora = None
        self.local = None
    
    #Usa como referencia os objetos vazios passados no __init__ para receber novos valores, que será feita no arquivo menu.py.
    def coleta_dados(self, pdetalhes, pdia, phora, plocal):
        self.detalhes = pdetalhes
        self.dia = pdia
        self.hora = phora
        self.local = plocal
        self.salvar()
        
    #Método para salvar as informações obtidas nos inputs na tabela do banco de dados criado, retorna erro caso não seja sucedido.
    def salvar (self):
        try:
            cnx = mysql.connector.connect(host='localhost', database='db_todo_list', user='root', password='1234')
            cursor = cnx.cursor()
            inserir_tarefas = "insert into tarefas (detalhes, dia, hora, local) values (%s, %s, %s, %s)"
            dados = (self.detalhes, self.dia, self.hora, self.local)
            cursor.execute(inserir_tarefas, dados)
            cnx.commit()
            print('Adicionado com sucesso!')
            
        except Error as erro:
            print('Não foi possível conectar ao banco de dados', erro)
                
                
    #Método para visualizar os dados salvos na tabela.
    def Verificar(self):
        try:
            cnx = mysql.connector.connect(host='localhost', database='db_todo_list', user='root',password='1234')
            consulta = "select * from tarefas"
            cursor = cnx.cursor()
            cursor.execute(consulta)
            linhas = cursor.fetchall()
            print("Há ", cursor.rowcount, " tarefas salvas\n")
            for x in linhas:
                print("ID: ", x[0])
                print("Detalhes: ", x[1])
                print("Dia: ", x[2])
                print("Horário: ", x[3])
                print("Local: ", x[4], '\n')
        except Error as erro:
            print("Não foi possível conectar ao banco de dados", erro)
    
    #Método para deletar os dados com base no id.
    def Deletar(self, id):
        try:
            cnx = mysql.connector.connect(host='localhost', database='db_todo_list', user='root',password='1234')
            cursor = cnx.cursor()
            deletar = "delete from tarefas where id = %s"
            self.id = id
            cursor.execute(deletar, (self.id,))
            cnx.commit()
            print('Tarefa removida com sucesso!')
        except Error as erro:
            print('Houve um erro ao realizar a ação:', erro)
        
        