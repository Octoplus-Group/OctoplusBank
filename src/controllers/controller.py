
from flask.views import MethodView
from flask import request, render_template,redirect
from src.db import mysql


class IndexController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente")
            data = cur.fetchall()        
        return render_template('public/index.html', data=data)

    def post(self):

        nome = request.form['nome']
        CPF = request.form['CPF']
        dataNascimento = request.form['dataNascimento']
        genero = request.form['genero']
        telefone = request.form['telefone']
        cep = request.form['cep']
        cidade = request.form['cidade']
        endereco = request.form['endereco']
        bairro = request.form['bairro']
        numeroCasa = request.form['numeroCasa']
        tipoConta = request.form['tipoConta']
        senha = request.form['senha']
        

        with mysql.cursor()as cur:
            cur.execute("INSERT INTO cliente(NOME,CPF,DATA_NASCIMENTO,GENERO,TELEFONE,CEP,CIDADE,ENDERECO,BAIRRO,NUMERO,SENHA) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(nome,CPF,dataNascimento,genero,telefone,cep,cidade,endereco,bairro,numeroCasa,senha))
            cur.connection.commit()
            cur.execute("INSERT INTO conta (DATA_ABERTURA,TIPO_CONTA) VALUES (CURDATE(),%s)",(tipoConta))
            cur.connection.commit()
            cur.execute("SELECT ID_CONTA FROM conta ORDER BY ID_CONTA DESC")
            numeroconta=cur.fetchone()
            cur.execute("SELECT ID_CLIENTE FROM cliente ORDER BY ID_CLIENTE DESC")
            numerocliente=cur.fetchone()
            cur.execute("UPDATE cliente SET ID_CONTA =%s WHERE ID_CLIENTE = %s",(numeroconta,numerocliente))
            cur.connection.commit()
            mensagem="A sua conta está pendente de aprovação pelo gerente!"


            return render_template('public/cadastro_cliente.html', mensagem=mensagem)

class DeleteClienteController(MethodView):
    def post(self, id):
        with mysql.cursor()as cur:
            cur.execute("DELETE FROM cliente WHERE id =%s",(id))
            cur.connection.commit()
            return redirect('/')

class UpdateClienteController(MethodView):
    def get(self, id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s",(id))
            conta = cur.fetchone()
            return render_template('public/alteracao_dados.html', cliente=cliente, conta=conta)

    def post(self,id):

        nome = request.form['nome']
        CPF = request.form['CPF']
        dataNascimento = request.form['dataNascimento']
        genero = request.form['genero']
        telefone = request.form['telefone']
        cep = request.form['cep']
        cidade = request.form['cidade']
        endereco = request.form['endereco']
        bairro = request.form['bairro']
        numeroCasa = request.form['numeroCasa']
        tipoConta = request.form['tipoConta']
        senha = request.form['senha']
        
        with mysql.cursor() as cur:
            cur.execute("UPDATE cliente SET NOME =%s,CPF =%s,DATA_NASCIMENTO =%s,GENERO =%s,TELEFONE =%s,CEP =%s,CIDADE =%s,ENDERECO =%s,BAIRRO =%s,NUMERO =%s,SENHA =%s WHERE  ID_CLIENTE = %s",(nome,CPF,dataNascimento,genero,telefone,cep,cidade,endereco,bairro,numeroCasa,senha,id))
            cur.connection.commit()
            cur.execute("UPDATE conta SET TIPO_CONTA =%s WHERE ID_CONTA = %s",(tipoConta,id))
            cur.connection.commit()

            return redirect('/')

class CadastroClienteController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente")
            data = cur.fetchall()
            """ cur.execute("SELECT id FROM cliente ORDER BY id DESC LIMIT 1")
            numeroconta=cur.fetchone() ANTIGO INCREMENTO DE NUMERO DE CONTA """ 
        return render_template('public/cadastro_cliente.html', data=data)

class LoginController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente")
            data = cur.fetchall()
        return render_template('public/Login.html', data=data)

class LoginValicaoController(MethodView):
    def post(self):
        agencia=request.form['agencia']
        id=request.form['id']
        senhalogin = request.form['senha']

        with mysql.cursor() as cur:
            cur.execute("SELECT ID_CONTA FROM cliente WHERE ID_CONTA=%s AND ID_AGENCIA=%s",(id,agencia))
            cliente = cur.fetchone()
            if cliente!= None:
                cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
                cliente = cur.fetchone()
                if senhalogin == cliente[12] and cliente[14]=='CL' and cliente[13]=='APROVADO':
                    cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
                    cliente = cur.fetchone()
                    cur.execute("SELECT * FROM conta  WHERE ID_CONTA =%s",(id))
                    conta = cur.fetchone()
                    return render_template('public/home_user.html', cliente=cliente, conta=conta)
                elif senhalogin == cliente[12] and cliente[14]=='GA' and cliente[13]=='APROVADO':
                    cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
                    cliente = cur.fetchone()
                    cur.execute("SELECT * FROM conta  WHERE ID_CONTA =%s",(id))
                    conta = cur.fetchone()
                    return render_template('public/home_gerente.html', cliente=cliente, conta=conta)
                else:
                    return render_template('public/Login.html')

    
            else:
                return render_template('public/Login.html')

class HomeUserController(MethodView):
    def get(self, id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE id =%s",(id))
            cliente = cur.fetchone()
        return render_template('public/home_user.html' , cliente=cliente)

class DadosController(MethodView):
    def get(self,id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s",(id))
            conta = cur.fetchone()
        return render_template('public/dados.html' , cliente=cliente, conta=conta)

class paginaDepositoController(MethodView):
    def get(self,id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA = %s",(cliente[0]))
            conta = cur.fetchone()
            mensagem=''
        return render_template('public/deposito.html', cliente=cliente, conta=conta, mensagem=mensagem)

class realizarDepositoController(MethodView):
    def post(self,id):
        deposito = float(request.form['deposito'])
               
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA = %s",(cliente[0]))
            conta = cur.fetchone()
            saldofinal = deposito

            cur.execute("INSERT INTO transacoes (ID_CONTA,TIPO,DATA,VALOR) VALUES (%s,'DEPOSITO',CURDATE(),%s)",(cliente[0],saldofinal))
            cur.connection.commit()
            mensagem='Deposito em analise pelo Gerente'

            """ cur.execute("UPDATE conta SET saldo =%s WHERE  ID_CONTA = %s",(saldofinal,cliente[0]))
            cur.connection.commit() """
        return render_template('public/deposito.html', cliente=cliente , conta=conta , mensagem=mensagem)

class paginaSaqueController(MethodView):
    def get(self,id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA = %s",(cliente[0]))
            conta = cur.fetchone()
            mensagem =''
        return render_template('public/saque.html', cliente=cliente, conta=conta,mensagem=mensagem )

class realizarSaqueController(MethodView):
    def post(self,id):
        saque = float(request.form['saque'])*(-1)
               
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s",(id))
            conta = cur.fetchone()
            saldofinal = ((saque)+(conta[4]))
            cur.execute("UPDATE conta SET saldo =%s WHERE  ID_CONTA =%s",(saldofinal,id))
            cur.connection.commit()
            cur.execute("INSERT INTO transacoes (ID_CONTA,TIPO,DATA,VALOR,STATUS) VALUES (%s,'SAQUE',CURDATE(),%s,'APROVADO')",(conta[1],saque))
            cur.connection.commit()
            mensagem='Saque Realizado com Sucesso'
        return render_template('public/saque.html',cliente=cliente, conta=conta,mensagem=mensagem )

class HomeUserIDController(MethodView):
    def get(self, id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s",(id))
            conta = cur.fetchone()
            return render_template('public/home_user.html', cliente=cliente, conta = conta)

class HomeGerenteAgenciaController(MethodView):
    def get(self,id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s",(id))
            conta = cur.fetchone()
            return render_template('public/home_gerente.html', cliente=cliente, conta = conta)

class LinkGerenciarContasController(MethodView):
    def get(self,id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s",(id))
            conta = cur.fetchone()
            cur.execute("SELECT * FROM cliente WHERE STATUS =%s",('APROVADO'))
            dataAprovado = cur.fetchall()
            cur.execute("SELECT * FROM cliente WHERE STATUS =%s",('ANALISE'))
            dataAnalise = cur.fetchall()

            return render_template('public/gerenciar_contas.html', cliente=cliente, conta = conta, dataAprovado=dataAprovado, dataAnalise=dataAnalise)

class AprovacaoContaController(MethodView):
    def get(self,id):
        with mysql.cursor() as cur:
            
            cur.execute("UPDATE cliente SET STATUS =%s WHERE  ID_CLIENTE = %s",('APROVADO',id))
            cur.connection.commit()
            cur.execute("SELECT * FROM cliente WHERE STATUS =%s",('APROVADO'))
            dataAprovado = cur.fetchall()
            cur.execute("SELECT * FROM cliente WHERE STATUS =%s",('ANALISE'))
            dataAnalise = cur.fetchall()
            cur.execute("SELECT * FROM cliente WHERE FUNCAO ='GA'")
            cliente = cur.fetchone()
        
            return render_template('public/gerenciar_contas.html', cliente=cliente , dataAprovado=dataAprovado, dataAnalise=dataAnalise)

class ModoGerenteAgenciaController(MethodView):
    def get(self,id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s",(id))
            conta = cur.fetchone()
            return render_template('public/modo_gerente.html', cliente=cliente, conta = conta)

class LinkAprovacaoDepositoController(MethodView):
    def get(self,id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s",(id))
            conta = cur.fetchone()
            cur.execute("SELECT * FROM transacoes WHERE STATUS =%s",('APROVADO'))
            depositoAprovado = cur.fetchall()
            cur.execute("SELECT * FROM transacoes WHERE STATUS =%s",('ANALISE'))
            depositoAnalise = cur.fetchall()

            return render_template('public/aprovar_depositos.html', cliente=cliente, conta = conta, depositoAprovado=depositoAprovado, depositoAnalise=depositoAnalise)

class ExecucaoDepositoController(MethodView):
    def get(self,id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * from transacoes WHERE ID_TRANSACAO =%s",(id))
            deposito=cur.fetchone()
            cur.execute("SELECT * from conta WHERE ID_CONTA =%s",(deposito[0]))
            depositoEtapa=cur.fetchone()
            depositoreal=depositoEtapa[4]+deposito[4]
            cur.execute("UPDATE conta SET SALDO =%s  WHERE ID_CONTA =%s ",(depositoreal,deposito[0]))
            cur.execute("UPDATE transacoes SET STATUS =%s  WHERE ID_TRANSACAO =%s ",('APROVADO',id))
            cur.execute("SELECT * FROM cliente WHERE FUNCAO ='GA'")
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM transacoes WHERE STATUS =%s",('ANALISE'))
            depositoAnalise = cur.fetchall()

            return render_template('public/aprovar_depositos.html', cliente=cliente, depositoAnalise=depositoAnalise)

class LinkExtratoController(MethodView):
    def get(self,id):           
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s",(id))
            conta = cur.fetchone()
            extrato=''

            return render_template('public/extrato.html', cliente=cliente , conta=conta,extrato=extrato)

class GerarExtratoController(MethodView):
    def post(self,id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s",(id))
            conta = cur.fetchone()
            inicio = request.form['inicioExtrato']
            fim = request.form['fimExtrato']
            print('Tipo data',inicio)
            print('Tipo data',fim)
            cur.execute("SELECT * FROM transacoes WHERE DATA between  %s AND %s and ID_CONTA =%s",(inicio,fim,id))
            extrato=cur.fetchall()

            return render_template('public/extrato.html',extrato=extrato, cliente=cliente , conta=conta)


class paginaDepositoGerenteController(MethodView):
    def get(self,id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CLIENTE =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA = %s",(cliente[0]))
            conta = cur.fetchone()
            mensagem=''
        return render_template('public/deposito_gerente.html', cliente=cliente, conta=conta,mensagem=mensagem)

class realizarDepositoGerenteController(MethodView):
    def post(self,id):
        deposito = float(request.form['deposito'])
               
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CLIENTE =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA = %s",(cliente[0]))
            conta = cur.fetchone()
            saldofinal = deposito
            mensagem='Deposito em Analise pelo Gerente'

            cur.execute("INSERT INTO transacoes (ID_CONTA,TIPO,DATA,VALOR) VALUES (%s,'DEPOSITO',CURDATE(),%s)",(cliente[0],saldofinal))
            cur.connection.commit()

            """ cur.execute("UPDATE conta SET saldo =%s WHERE  ID_CONTA = %s",(saldofinal,cliente[0]))
            cur.connection.commit() """
        return render_template('public/deposito_gerente.html', cliente=cliente, conta=conta,mensagem=mensagem)

class paginaSaqueGerenteController(MethodView):
    def get(self,id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CLIENTE =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA = %s",(cliente[0]))
            conta = cur.fetchone()
            mensagem=''
        return render_template('public/saque_gerente.html', cliente=cliente, conta=conta,mensagem=mensagem)

class realizarSaqueGerenteController(MethodView):
    def post(self,id):
        saque = float(request.form['saque'])*(-1)
               
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CLIENTE =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s",(id))
            conta = cur.fetchone()
            saldofinal = ((saque)+(conta[4]))
            cur.execute("UPDATE conta SET saldo =%s WHERE  ID_CONTA =%s",(saldofinal,id))
            cur.connection.commit()
            cur.execute("INSERT INTO transacoes (ID_CONTA,TIPO,DATA,VALOR,STATUS) VALUES (%s,'SAQUE',CURDATE(),%s,'APROVADO')",(conta[1],saque))
            cur.connection.commit()
            mensagem='Saque Realizado com Sucesso !'
        return render_template('public/saque_gerente.html', cliente=cliente, conta=conta,mensagem=mensagem)

class HomeGerenteContaController(MethodView):
    def get(self,id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CLIENTE =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA = %s",(cliente[0]))
            conta = cur.fetchone()
            return render_template('public/home_gerente_conta.html', cliente=cliente, conta=conta)
        
    
