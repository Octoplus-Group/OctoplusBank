import mysql.connector
passw = input("Sua senha do banco de dados: ")
octbd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = f"{passw}",
    database = "octoplus_bank")

import datetime
x = datetime.datetime.now()
data = (x.strftime("%Y-%m-%d %H:%M"))

tipo = input("Tipo de transação: ")
s = "Saque"
d = "Depósito"
for t in tipo:
    if s == tipo or d == tipo:
        break
    else:
        tipo = input("Inserir se a transação é Saque/Depósito")

valor = input("Valor da transação: R$")
v = len(valor)
v
for x in valor:
    if v <= 11:
        break
    else:
        valor = input("Digite um valor menor: R$")
        v = len(valor)
        v

cursor = octbd.cursor()

inserir = "INSERT INTO transacoes (TIPO, DATA, VALOR) VALUES (%s, %s, %s)"
val = (f"{tipo}", f"{data}", f"{valor}")

cursor.execute(inserir, val)

octbd.commit()

print(f"Um {tipo} de R${valor} foi realizado na data {data}")
