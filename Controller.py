'''O arquivo Controller terá as requisições do usuário'''
import mysql.connector

conexao = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database = "loja"
)

def mostrarAoUsuario():
    acao = conexao.cursor()

    comando = input("O que deseja fazer no Banco de Dados: ")

    if comando == "mostrar":
            acao.execute("SELECT * FROM produto")
            result = acao.fetchall()#Essa função busca todas as linhas da última instrução executada
            print(result)