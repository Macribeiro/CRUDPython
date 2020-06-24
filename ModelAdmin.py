'''O arquivo ModelAdmin vai servir como se fosse alguma pessoa DBA no sistema da loja
onde ele vai poder criar um banco de dados, criar tabelas,  apagar colunas e tabelas, etc'''
import mysql.connector
import ModelGerente as mg
#O import aqui funciona como o import do Java. Aqui eu estou importando outros arquivos para que eu possa usá-los aqui


conexao = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database = "loja" #criei um banco chamado de loja no MySQL Workbench, mas aqui tem a opção de criar, porém está tudo pré setado (para que o projeto dê certo)
)

acao = conexao.cursor()

def modificacaoAdmin():
  comando = input("O que deseja fazer no Banco de Dados: ")

  if comando == "criar banco de dados":
      #Aqui será o comando que criara o banco de dados
      acao.execute("CREATE DATABASE loja")
      #a função execute executa no banco de dados a ação descrita acima
  elif comando == "criar tabela":#Aqui será o comando que irá criar a tabela no banco de dados
      acao.execute("CREATE TABLE produto (idproduto VARCHAR(10), descricaoproduto VARCHAR(100), precoproduto VARCHAR(25))")
  elif comando == "mostrar bancos":#Aqui será o comando que irá mostrar os bancos de dados
      acao.execute("SHOW DATABASES")
      for x in acao:
          print(x) #aqui mostra os bancos
  elif comando == "apagar":#Aqui será o comando que irá deletar dados da tabela "produto" no banco de dados
    deletar = "DELETE FROM produto WHERE precoproduto = 'R$20.00'"
    acao.execute(deletar)
    conexao.commit()
    print(acao.rowcount, "gravura(s) deleteda(s)")
  elif comando == "apagar tabela":#Aqui será o comando que irá deletar a tabela no banco de dados
    acao.execute("DROP TABLE produto")
  elif comando == "apagar coluna":#Aqui será o comando que irá deletar a coluna da tabela "produto"
      coluna = "DELETE FROM produto WHERE %s = %s"
      aviso = input("Digite a coluna que deseja apagar: ")
      aviso2 = input("Valor atribuido a coluna desejada: ")
      val = (aviso,aviso2)
      acao.execute(coluna,val)
      conexao.commit()


opcao = input("Você está agindo como Administrador. O que deseja fazer? ")

if opcao == "gerente":
  mg.modificacaoGerente()
elif opcao == "admin":
  modificacaoAdmin()