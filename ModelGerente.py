'''O arquivo ModelGerente vai ser usado como se fosse o gerente da loja, onde ele só vai
inserir produtos e atualizar eles'''
import mysql.connector

conexao = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database = "loja" 
)

acao = conexao.cursor()

def modificacaoGerente():
  comando = input("O que deseja fazer no Banco de Dados: ")
  if comando == "inserir":#Aqui será o comando que irá inserir dados na tabela "produto"
      try:
          inserir = "INSERT INTO produto (idproduto, descricaoproduto, precoproduto) VALUES (%s, %s, %s)"
          idProduto = input("ID produto: ")
          descProduto = input("Descrição do Produto: ")
          precoProduto = input("Valor do Produto: ")
          val = (idProduto,descProduto,"R$" + precoProduto)
          acao.execute(inserir, val)
          conexao.commit()#A função commit é necessária para que seja validado, caso contrário não haveria inserção
          print(acao.rowcount, "gravura inserida.")
      except:
          print("Algo deu errado.")
  elif comando == "atualizar":#Aqui será o comando que irá atualizar os dados na tabela "produto"
    atualizarTabela = "UPDATE produto SET precoproduto = %s WHERE idproduto = %s"
    novoValor = input("Novo dado inserido: ")
    localizar = input("Onde esse dado está guardado: ")
    valAtt = (novoValor,localizar)
    acao.execute(atualizarTabela, valAtt)
    conexao.commit()
    print(acao.rowcount, "gravura(s) afetada(s)")