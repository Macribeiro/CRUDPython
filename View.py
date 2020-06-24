#Esse arquivo seria somente o que o usúario iria ver
import mysql.connector
import Controller as c
#O import aqui funciona como o import do Java. Aqui eu estou importando outros arquivos para que eu possa usá-los aqui

#Aqui ocorre a conexão com o Banco de Dados
conexao = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database = "loja" 
)

c.mostrarAoUsuario()