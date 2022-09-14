#conector mysql
import mysql.connector
octbd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "fatec",
    database = "octoplus_bank")

#inserção de dados
nome = input("Nome: ")
cpf = int(input("CPF: "))
data_nasc = input("Data de nascimento aaaa-mm-dd: ")
genero = input("Gênero(Masculino, Feminino, Outro): ")
tel = int(input("Telefone: "))
cep = int(input("CEP: "))
cidade = input("Cidade: ")
bairro = input("Bairro: ")
endereço = input("Logradouro: ")
numero = int(input("N°: "))
senha = input("Senha: ")

#indica onde estaria o cursor
cursor = octbd.cursor()

inserir = "insert INTO cliente (NOME, CPF, DATA_NASCIMENTO, GENERO, TELEFONE, CEP, ENDERECO, CIDADE, BAIRRO, NUMERO, SENHA) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = (f"{nome}", f"{cpf}", f"{data_nasc}", f"{genero}", f"{tel}", f"{cep}", f"{endereço}", f"{cidade}", f"{bairro}", f"{numero}", f"{senha}")

#executa a linha onde o cursor está
cursor.execute(inserir, val)

#dá o commit para a tabela
octbd.commit()

print(f"Cliente {nome} foi inserido!")
