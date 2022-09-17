import mysql.connector
passw = input("Sua senha do banco de dados: ")
octbd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = f"{passw}",
    database = "octoplus_bank")

import datetime
x = datetime.datetime.now()
data = (x.strftime("%Y-%m-%d"))
valor = input("Valor do depósito: R$")
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

inserir = "INSERT INTO transacoes (DATA, VALOR) VALUES (%s, %s)"
val = (f"{data}", f"{valor}")

cursor.execute(inserir, val)

octbd.commit()

print(f"Um valor de R${valor} foi depositado na data {data}")
