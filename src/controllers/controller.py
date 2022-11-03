
from operator import methodcaller
from flask.views import MethodView
from flask import request, render_template,redirect
from src.db import mysql
import datetime

data_atual= datetime.date.today()


class IndexController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM banco")
            data = cur.fetchall()
            cur.execute("SELECT * FROM banco where ID_BANCO=%s ",(1))
            banco=cur.fetchone()
        return render_template('public/index.html', data=data, banco=banco)

    def post(self):

        capitalbanco = request.form['capitalInicial']
        jurosPoupanca = request.form['jurosPoupanca']
        jurosCheque = request.form['jurosCheque']
        
        
        
        with mysql.cursor()as cur:
            cur.execute("UPDATE banco SET CAPITAL_TOTAL =%s, JUROS_POUPANCA=%s, JUROS_CQ=%s  WHERE ID_BANCO = %s",(capitalbanco,jurosPoupanca,jurosCheque,1))
            cur.connection.commit()
            mensagem="A sua conta está pendente de aprovação pelo gerente!"


            return render_template('public/area_cliente.html', mensagem=mensagem)

class AreaClienteController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM banco")
            data = cur.fetchall()
            cur.execute("SELECT * FROM banco where ID_BANCO=%s ",(1))
            banco=cur.fetchone()
            
        return render_template('public/area_cliente.html', data=data, banco=banco)

    def post(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente")
            data = cur.fetchall()
            cur.execute("SELECT ID_CONTA FROM conta ORDER BY ID_CONTA DESC")
            numeroconta=cur.fetchone()
            cur.execute("SELECT ID_CLIENTE FROM cliente ORDER BY ID_CLIENTE DESC")
            numerocliente=cur.fetchone()
        return render_template('public/index.html', data=data, numeroconta=numeroconta , numerocliente=numerocliente)

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
            cur.execute("INSERT INTO conta (DATA_ABERTURA,TIPO_CONTA) VALUES (NOW(),%s)",(tipoConta))
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
    def get(self, id):
        
        with mysql.cursor() as cur:
            
            cur.execute("DELETE from cliente WHERE ID_CLIENTE =%s",(id))
            cur.connection.commit()
            cur.execute("SELECT * FROM cliente WHERE STATUS =%s",('APROVADO'))
            dataAprovado = cur.fetchall()
            cur.execute("SELECT * FROM cliente WHERE STATUS =%s",('ANALISE'))
            dataAnalise = cur.fetchall()
            cur.execute("SELECT * FROM cliente WHERE FUNCAO ='GA'")
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM cliente WHERE REQUISICAO =%s",('DELETAR'))
            dataDeletar = cur.fetchall()
        
            return render_template('public/gerenciar_contas.html', cliente=cliente , dataAprovado=dataAprovado, dataAnalise=dataAnalise, dataDeletar=dataDeletar)

class DeleteClienteRequisicaoController(MethodView):
    def get(self, id):
        with mysql.cursor()as cur:
            cur.execute("UPDATE cliente SET REQUISICAO =%s WHERE ID_CLIENTE =%s",('DELETAR',id))
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
            cur.execute("UPDATE cliente SET NOME =%s,CPF =%s,DATA_NASCIMENTO =%s,GENERO =%s,TELEFONE =%s,CEP =%s,CIDADE =%s,ENDERECO =%s,BAIRRO =%s,NUMERO =%s,SENHA =%s WHERE  ID_CONTA = %s",(nome,CPF,dataNascimento,genero,telefone,cep,cidade,endereco,bairro,numeroCasa,senha,id))
            cur.connection.commit()
            cur.execute("UPDATE conta SET TIPO_CONTA =%s WHERE ID_CONTA = %s",(tipoConta,id))
            cur.connection.commit()

            return redirect('/')

class UpdateGerenteController(MethodView):
    def get(self, id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s",(id))
            conta = cur.fetchone()
            return render_template('public/alteracao_dados_gerente.html', cliente=cliente, conta=conta)

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
            cur.execute("UPDATE cliente SET NOME =%s,CPF =%s,DATA_NASCIMENTO =%s,GENERO =%s,TELEFONE =%s,CEP =%s,CIDADE =%s,ENDERECO =%s,BAIRRO =%s,NUMERO =%s,SENHA =%s WHERE  ID_CONTA = %s",(nome,CPF,dataNascimento,genero,telefone,cep,cidade,endereco,bairro,numeroCasa,senha,id))
            cur.connection.commit()
            cur.execute("UPDATE conta SET TIPO_CONTA =%s WHERE ID_CONTA = %s",(tipoConta,id))
            cur.connection.commit()

            cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s",(id))
            conta = cur.fetchone()
            return render_template('public/alteracao_dados_gerente.html', cliente=cliente, conta=conta)

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
                elif senhalogin == cliente[12] and cliente[14]=='GG' and cliente[13]=='APROVADO':
                    cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
                    cliente = cur.fetchone()
                    cur.execute("SELECT * FROM conta  WHERE ID_CONTA =%s",(id))
                    conta = cur.fetchone()
                    return render_template('public/home_gerente_geral.html', cliente=cliente, conta=conta)
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

            cur.execute("INSERT INTO transacoes (ID_CONTA,TIPO,DATA,VALOR) VALUES (%s,'DEPOSITO',NOW(),%s)",(cliente[0],saldofinal))
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
            cur.execute("SELECT * FROM banco WHERE ID_BANCO =%s",(1))
            banco = cur.fetchone()
            cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s",(id))
            conta = cur.fetchone()
            capital = float(banco[2])
            saque = saque*-1

            if saque>capital:
                mensagem = 'Saque não pode ser realizado, favor entrar em contato com o Gerente de Geral'
                return render_template('public/saque.html', cliente=cliente, conta=conta,mensagem=mensagem)
            else:
                with mysql.cursor() as cur:
                    saque = saque * -1 
                    cur.execute("SELECT * FROM banco WHERE ID_BANCO =%s",(1))
                    banco = cur.fetchone()
                    cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
                    cliente = cur.fetchone()
                    cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s",(id))
                    conta = cur.fetchone()
                    saldofinal = ((saque)+(conta[4]))
                    capitalfinalBanco = banco[2]+saque
                    cur.execute("UPDATE conta SET saldo =%s WHERE  ID_CONTA =%s",(saldofinal,id))
                    cur.connection.commit()
                    cur.execute("UPDATE banco SET CAPITAL_TOTAL =%s WHERE  ID_BANCO =%s",(capitalfinalBanco,1))
                    cur.connection.commit()
                    cur.execute("INSERT INTO transacoes (ID_CONTA,TIPO,DATA,VALOR,STATUS) VALUES (%s,'SAQUE',NOW(),%s,'APROVADO')",(conta[1],saque))
                    cur.connection.commit()
                    mensagem='Saque Realizado com Sucesso'
                return render_template('public/saque.html', cliente=cliente, conta=conta,mensagem=mensagem)

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

class HomeGerenteGeralController(MethodView):
    def get(self,id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s",(id))
            conta = cur.fetchone()
            return render_template('public/home_gerente_geral.html', cliente=cliente, conta = conta)

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
            cur.execute("SELECT * FROM cliente WHERE REQUISICAO =%s",('DELETAR'))
            dataDeletar = cur.fetchall()

            return render_template('public/gerenciar_contas.html', cliente=cliente, conta = conta, dataAprovado=dataAprovado, dataAnalise=dataAnalise, dataDeletar=dataDeletar)

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

class LinkExtratoGerenteController(MethodView):
    def get(self,id):           
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s",(id))
            conta = cur.fetchone()
            extrato=''

            return render_template('public/extrato_gerente.html', cliente=cliente , conta=conta,extrato=extrato)

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
            cur.execute("SELECT * FROM transacoes WHERE DATA between  %s'00:00:00' AND %s'23:59:59' and ID_CONTA =%s",(inicio,fim,id))
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

            cur.execute("INSERT INTO transacoes (ID_CONTA,TIPO,DATA,VALOR) VALUES (%s,'DEPOSITO',NOW(),%s)",(cliente[0],saldofinal))
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
            cur.execute("SELECT * FROM banco WHERE ID_BANCO =%s",(1))
            banco = cur.fetchone()
            cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s",(id))
            conta = cur.fetchone()
            capital = float(banco[2])
            saque = saque*-1

            if saque>capital:
                mensagem = 'Saque não pode ser realizado, favor entrar em contato com o Gerente de Geral'
                return render_template('public/saque_gerente.html', cliente=cliente, conta=conta,mensagem=mensagem)
            else:
                with mysql.cursor() as cur:
                    saque = saque * -1 
                    cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
                    cliente = cur.fetchone()
                    cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s",(id))
                    conta = cur.fetchone()
                    saldofinal = ((saque)+(conta[4]))
                    capitalfinalBanco = banco[2]+saque
                    cur.execute("UPDATE conta SET saldo =%s WHERE  ID_CONTA =%s",(saldofinal,id))
                    cur.connection.commit()
                    cur.execute("UPDATE banco SET CAPITAL_TOTAL =%s WHERE  ID_BANCO =%s",(capitalfinalBanco,1))
                    cur.connection.commit()
                    cur.execute("UPDATE conta SET saldo =%s WHERE  ID_CONTA =%s",(saldofinal,id))
                    cur.connection.commit()
                    cur.execute("INSERT INTO transacoes (ID_CONTA,TIPO,DATA,VALOR,STATUS) VALUES (%s,'SAQUE',NOW(),%s,'APROVADO')",(conta[1],saque))
                    cur.connection.commit()
                    mensagem='Saque Realizado com Sucesso'
                return render_template('public/saque_gerente.html', cliente=cliente, conta=conta,mensagem=mensagem)

class HomeGerenteContaController(MethodView):
    def get(self,id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CLIENTE =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA = %s",(cliente[0]))
            conta = cur.fetchone()
            return render_template('public/home_gerente_conta.html', cliente=cliente, conta=conta)

class LinkPaginaCadastroController(MethodView):

    def get(self):
        
        with mysql.cursor()as cur:
            cur.execute("SELECT * FROM conta ORDER BY ID_CONTA DESC")
            numerocontaAbertura=cur.fetchone()
            cur.execute("SELECT * FROM cliente ORDER BY ID_CLIENTE DESC")
            numeroclienteAbertura=cur.fetchone()
            cur.execute("SELECT ID_CONTA FROM conta ORDER BY ID_CONTA DESC")
            numeroconta=cur.fetchone()
            cur.execute("SELECT ID_CLIENTE FROM cliente ORDER BY ID_CLIENTE DESC")
            numerocliente=cur.fetchone()
            cur.execute("UPDATE cliente SET ID_CONTA =%s WHERE ID_CLIENTE = %s",(numeroconta,numerocliente))
            cur.connection.commit()
            print('esta passando',numeroconta)
            

            return render_template('/public/cadastro_cliente.html', numeroclienteAbertura=numeroclienteAbertura , numerocontaAbertura=numerocontaAbertura)

class CadastroClienteController(MethodView):
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
        nome = nome.upper()
        
        with mysql.cursor()as cur:
            cur.execute("INSERT INTO cliente(NOME,CPF,DATA_NASCIMENTO,GENERO,TELEFONE,CEP,CIDADE,ENDERECO,BAIRRO,NUMERO,SENHA) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(nome,CPF,dataNascimento,genero,telefone,cep,cidade,endereco,bairro,numeroCasa,senha))
            cur.connection.commit()
            cur.execute("INSERT INTO conta (DATA_ABERTURA,TIPO_CONTA) VALUES (NOW(),%s)",(tipoConta))
            cur.connection.commit()
            cur.execute("SELECT ID_CONTA FROM conta ORDER BY ID_CONTA DESC")
            numeroconta=cur.fetchone()
            cur.execute("SELECT ID_CLIENTE FROM cliente ORDER BY ID_CLIENTE DESC")
            numerocliente=cur.fetchone()
            cur.execute("SELECT * FROM conta ORDER BY ID_CONTA DESC")
            numerocontaAbertura=cur.fetchone()
            cur.execute("SELECT * FROM cliente ORDER BY ID_CLIENTE DESC")
            numeroclienteAbertura=cur.fetchone()
            cur.execute("UPDATE cliente SET ID_CONTA =%s WHERE ID_CLIENTE = %s",(numeroconta,numerocliente))
            cur.connection.commit()
            mensagem = 'Sua conta está sendo verificada! Clique em verificar novamente para ver se a sua conta ja foi aprovada ! ;)'
            
            return render_template('/public/aguardandoAprovacao.html', numerocontaAbertura=numerocontaAbertura, numeroclienteAbertura=numeroclienteAbertura,mensagem=mensagem)    


class VerificacaoAprovacao(MethodView):
    def get(self):
        with mysql.cursor()as cur:
            cur.execute("SELECT * FROM conta ORDER BY ID_CONTA DESC")
            numerocontaAbertura=cur.fetchone()
            cur.execute("SELECT * FROM cliente ORDER BY ID_CLIENTE DESC")
            numeroclienteAbertura=cur.fetchone()
            mensagem = 'Sua conta está sendo verificada! Validaremos ela em 1 minuto, apenas aguarde...'
            return render_template('/public/aguardandoAprovacao.html', numerocontaAbertura=numerocontaAbertura, numeroclienteAbertura=numeroclienteAbertura,mensagem=mensagem)


class paginaTransferenciaController(MethodView):
    def get(self,id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA = %s",(cliente[0]))
            conta = cur.fetchone()
            mensagem=''
        return render_template('public/transferencia.html', cliente=cliente, conta=conta, mensagem=mensagem)


class realizarTransferenciaController(MethodView):
    def post(self, id):
        transferencia = float(request.form['transferencia'])
        agencia = request.form["agencia"]
        para = request.form["para"]
               
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s",(id))
            conta = cur.fetchone()
            saldofinal = ((transferencia * -1)+(conta[4]))
            cur.execute("UPDATE conta SET saldo =%s WHERE  ID_CONTA =%s",((saldofinal),id))
            cur.connection.commit()
            cur.execute("INSERT INTO transacoes (ID_CONTA,TIPO,DATA,VALOR,STATUS) VALUES (%s,'TRANSF.',NOW(),%s,'APROVADO')",(conta[1],transferencia  * -1))
            cur.connection.commit()

            cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s and ID_AGENCIA=%s",(para,agencia))
            conta = cur.fetchone()
            saldofinal = (transferencia + conta[4])
            cur.execute("UPDATE conta SET saldo =%s WHERE  ID_CONTA =%s AND ID_AGENCIA=%s",(saldofinal, para,agencia))
            cur.connection.commit()
            cur.execute("INSERT INTO transacoes (ID_CONTA,TIPO,DATA,VALOR,STATUS) VALUES (%s,'TRANSF.',NOW(),%s,'APROVADO')",(para, transferencia))
            cur.connection.commit()

            cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s",(id))
            conta = cur.fetchone()

            mensagem='Transferencia Realizada com Sucesso'

        return render_template('public/transferencia.html',cliente=cliente, conta=conta, mensagem=mensagem )



class paginaTransferenciaGerenteController(MethodView):
    def get(self,id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA = %s",(cliente[0]))
            conta = cur.fetchone()
            mensagem=''
        return render_template('public/transferencia_gerente.html', cliente=cliente, conta=conta, mensagem=mensagem)


class realizarTransferenciaGerenteController(MethodView):
    def post(self, id):
        transferencia = float(request.form['transferencia'])
        agencia = request.form["agencia"]
        para = request.form["para"]
               
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s",(id))
            conta = cur.fetchone()
            saldofinal = ((transferencia * -1)+(conta[4]))
            cur.execute("UPDATE conta SET saldo =%s WHERE  ID_CONTA =%s",((saldofinal),id))
            cur.connection.commit()
            cur.execute("INSERT INTO transacoes (ID_CONTA,TIPO,DATA,VALOR,STATUS) VALUES (%s,'TRANSF.',NOW(),%s,'APROVADO')",(conta[1],transferencia  * -1))
            cur.connection.commit()

            cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s and ID_AGENCIA=%s",(para,agencia))
            conta = cur.fetchone()
            saldofinal = (transferencia + conta[4])
            cur.execute("UPDATE conta SET saldo =%s WHERE  ID_CONTA =%s AND ID_AGENCIA=%s",(saldofinal, para,agencia))
            cur.connection.commit()
            cur.execute("INSERT INTO transacoes (ID_CONTA,TIPO,DATA,VALOR,STATUS) VALUES (%s,'TRANSF.',NOW(),%s,'APROVADO')",(para, transferencia))
            cur.connection.commit()

            cur.execute("SELECT * FROM cliente WHERE ID_CONTA =%s",(id))
            cliente = cur.fetchone()
            cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s",(id))
            conta = cur.fetchone()

            mensagem='Transferencia Realizada com Sucesso'

        return render_template('public/transferencia_gerente.html',cliente=cliente, conta=conta, mensagem=mensagem )


class LoginFuncionario(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente")
            data = cur.fetchall()
        return render_template('public/adm.html', data=data)

    def post(self):
        idFuncionario=request.form['idFuncionario']
        senhalogin = request.form['senha']
        

        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE ID_CLIENTE=%s ",(idFuncionario))
            cliente = cur.fetchone()
            if cliente!= None:
                cur.execute("SELECT * FROM cliente WHERE ID_CLIENTE =%s",(idFuncionario))
                cliente = cur.fetchone()
                if senhalogin == cliente[12] and cliente[14]=='GG':
                    cur.execute("SELECT * FROM cliente WHERE ID_CLIENTE =%s",(idFuncionario))
                    cliente = cur.fetchone()
                    return render_template('public/home_gerente_geral.html', cliente=cliente)
                elif senhalogin == cliente[12] and cliente[14]=='GA':
                    cur.execute("SELECT * FROM cliente WHERE ID_CLIENTE =%s",(idFuncionario))
                    cliente = cur.fetchone()
                    cur.execute("SELECT * FROM conta WHERE ID_CONTA =%s",(cliente[0]))
                    conta = cur.fetchone()
                    
                    return render_template('public/home_gerente.html', cliente=cliente,conta=conta)
                else:
                    return render_template('public/adm.html')
            else:
                return render_template('public/adm.html') 

class GerenciarAgenciaLinkController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM agencia")
            agencias = cur.fetchall()
            cur.execute("SELECT * FROM cliente WHERE FUNCAO =%s",('GA'))
            gerenteAgencia = cur.fetchall()
        return render_template('public/gerenciar_agencias.html', agencias=agencias, gerenteAgencia=gerenteAgencia)

class GerenciarGerentesLinkController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cliente WHERE FUNCAO =%s",('GA'))
            gerenteAgencia = cur.fetchall()
        return render_template('public/gerenciar_gerentes.html', gerenteAgencia=gerenteAgencia)

class GerenciarBancoLinkController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM banco WHERE ID_BANCO=%s ",(1))
            banco = cur.fetchone()
            capital = round(banco[2],2)
        return render_template('public/gerenciar_banco.html',banco=banco,capital=capital)

class CadastrarAgenciaController(MethodView):
    def post(self):
        nomeGA = request.form['GA']
        enderecoAG = request.form['ENDERECO']
        with mysql.cursor() as cur:
            cur.execute("INSERT INTO agencia(GERENTE,ENDERECO) VALUES (%s,%s)",(nomeGA,enderecoAG))
            cur.connection.commit()

            cur.execute("SELECT * FROM agencia")
            agencias = cur.fetchall()
            cur.execute("SELECT * FROM cliente WHERE FUNCAO =%s",('GA'))
            gerenteAgencia = cur.fetchall()
        return render_template('public/gerenciar_agencias.html', agencias=agencias , gerenteAgencia=gerenteAgencia)

class CadastroGerenteAgencia(MethodView):
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
        nome = nome.upper()
        
        with mysql.cursor()as cur:
            cur.execute("INSERT INTO cliente(NOME,CPF,DATA_NASCIMENTO,GENERO,TELEFONE,CEP,CIDADE,ENDERECO,BAIRRO,NUMERO,SENHA,STATUS,FUNCAO) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(nome,CPF,dataNascimento,genero,telefone,cep,cidade,endereco,bairro,numeroCasa,senha,'APROVADO','GA'))
            cur.connection.commit()
            cur.execute("INSERT INTO conta (DATA_ABERTURA,TIPO_CONTA) VALUES (NOW(),%s)",(tipoConta))
            cur.connection.commit()
            cur.execute("SELECT ID_CONTA FROM conta ORDER BY ID_CONTA DESC")
            numeroconta=cur.fetchone()
            cur.execute("SELECT ID_CLIENTE FROM cliente ORDER BY ID_CLIENTE DESC")
            numerocliente=cur.fetchone()
            cur.execute("SELECT * FROM conta ORDER BY ID_CONTA DESC")
            numerocontaAbertura=cur.fetchone()
            cur.execute("SELECT * FROM cliente ORDER BY ID_CLIENTE DESC")
            numeroclienteAbertura=cur.fetchone()
            cur.execute("UPDATE cliente SET ID_CONTA =%s WHERE ID_CLIENTE = %s",(numeroconta,numerocliente))
            cur.connection.commit()
            cur.execute("SELECT * FROM cliente WHERE FUNCAO =%s",('GA'))
            gerenteAgencia = cur.fetchall()

        return render_template('public/gerenciar_gerentes.html', gerenteAgencia=gerenteAgencia)

class AlterarCapitalJurosController(MethodView):
    def post(self):
        capitalAdicional = float(request.form['capital'])
        jurosPP = request.form['jurospp']
        jurosCE = request.form['jurosce']
        

        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM banco WHERE ID_BANCO=%s ",(1))
            banco = cur.fetchone()
            print('tipocapital',type(capitalAdicional))
            print('tipobanco',type(banco[2]))
            capitalNovo= banco[2]+capitalAdicional
            cur.execute("UPDATE banco SET CAPITAL_TOTAL=%s, JUROS_POUPANCA=%s, JUROS_CQ=%s WHERE ID_BANCO = %s",(capitalNovo,jurosPP,jurosCE,1))
            cur.connection.commit()
            cur.execute("SELECT * FROM banco WHERE ID_BANCO=%s ",(1))
            banco = cur.fetchone()
            capital = round(banco[2],2)

        return render_template('public/gerenciar_banco.html',banco=banco,capital=capital)

class VerificacaoEntrada(MethodView):
    def get (self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM banco WHERE ID_BANCO=%s ",(1))
            banco = cur.fetchone()
            if banco[2]>0:
                return render_template ('public/area_cliente.html')
            else:
                return render_template ('public/capital.html')