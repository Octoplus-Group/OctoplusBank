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
    cp = cpf.count("")-1
    cp
    for x in cpf:
        if cp <= 11:
            break
        else:
            cpf = input("Digite o CPF novamente: ")
            cp = cpf.count("")-1
            cp
data_nasc = input("Data de nascimento aaaa-mm-dd: ")
genero = input("Gênero(Masculino, Feminino, Outro): ")
tel = int(input("Telefone: "))
    t = tel.count("")-1
    t
    for x in tel:
        if t <= 15:
            break
        else:
            senha = input("Digite o telefone novamente: ")
            s = senha.count("")-1
            s
cep = int(input("CEP: "))
    ce = cep.count("")-1
    ce
    for x in cep:
        if ce <= 8:
            break
        else:
            cep = input("Digite o CEP novamente: ")
            ce = cep.count("")-1
            ce
cidade = input("Cidade: ")
bairro = input("Bairro: ")
endereço = input("Logradouro: ")
numero = int(input("N°: "))
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

inserir = "insert INTO cliente (NOME, CPF, DATA_NASCIMENTO, GENERO, TELEFONE, CEP, ENDERECO, CIDADE, BAIRRO, NUMERO, SENHA) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = (f"{nome}", f"{cpf}", f"{data_nasc}", f"{genero}", f"{tel}", f"{cep}", f"{endereço}", f"{cidade}", f"{bairro}", f"{numero}", f"{senha}")

#executa a linha onde o cursor está
cursor.execute(inserir, val)

#dá o commit para a tabela
octbd.commit()

print(f"Cliente {nome} foi inserido!")
