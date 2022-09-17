import mysql.connector
passw = input("Sua senha do banco de dados: ")
octbd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = f"{passw}",
    database = "octoplus_bank")

cpf = int(input("Incira um CPF: "))

cursor = octbd.cursor()

bus_cpf = f"SELECT * FROM cliente WHERE CPF = {cpf}"

cursor.execute(bus_cpf)

myresult = cursor.fetchall()

for x in myresult:
    print(x)
