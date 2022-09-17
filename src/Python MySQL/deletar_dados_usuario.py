import mysql.connector
passw = input("Sua senha do banco de dados: ")
octbd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = f"{passw}",
    database = "octoplus_bank")

cpf = int(input("Delete um usuário(CPF): "))

cursor = octbd.cursor()

del_cpf = f"DELETE FROM cliente WHERE CPF = {cpf}"

cursor.execute(del_cpf)

octbd.commit()

print(cursor.rowcount, "usuário deletado")
