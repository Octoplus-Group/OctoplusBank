#conector mysql
import mysql.connector
passw = input("Sua senha do banco de dados: ")
octbd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = f"{passw}",
    database = "octoplus_bank")

#coleta de dados
nome = input("Nome: ")
cpf = input("CPF: ")
f = len(cpf)
f
for x in cpf:
    if f <= 11:
        break
    else:
        cpf = input("Digite o CPF novamente: ")
        f = len(cpf)
        f
data_nasc = input("Data de nascimento aaaa-mm-dd: ")
genero = input("Gênero(Masculino, Feminino, Outro): ")
tel = input("Telefone: ")
t = len(tel)
t
for x in tel:
    if t <= 15:
        break
    else:
        senha = input("Digite o telefone novamente: ")
        s = len(tel)
        s
cep = input("CEP: ")
p = len(cep)
p
for x in cep:
    if p <= 8:
        break
    else:
        cep = input("Digite o CEP novamente: ")
        p = len(cep)
        p
cidade = input("Cidade: ")
bairro = input("Bairro: ")
endereço = input("Logradouro: ")
numero = input("N°: ")
senha = input("Senha: ")
s = senha.count("")-1
s
for x in senha:
    if s <= 6:
        break
    else:
        senha = input("Digite uma senha menor: ")
        s = senha.count("")-1
        s

#indica onde estaria o cursor
cursor = octbd.cursor()

#inserção dos dados
inserir = "INSERT INTO cliente (NOME, CPF, DATA_NASCIMENTO, GENERO, TELEFONE, CEP, ENDERECO, CIDADE, BAIRRO, NUMERO, SENHA) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = (f"{nome}", f"{cpf}", f"{data_nasc}", f"{genero}", f"{tel}", f"{cep}", f"{endereço}", f"{cidade}", f"{bairro}", f"{numero}", f"{senha}")

#executa a linha onde está o cursor
cursor.execute(inserir, val)

#dá o commit para a tabela
octbd.commit()

print(f"Cliente {nome} foi inserido!")
