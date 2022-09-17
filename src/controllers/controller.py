from unicodedata import decimal
from flask.views import MethodView
from flask import request, render_template,redirect
from src.db import mysql


class IndexController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM clientes")
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
        saldo = request.form['saldo']

        with mysql.cursor()as cur:
            cur.execute("INSERT INTO clientes(nome,CPF,dataNascimento,genero,telefone,cep,cidade,endereco,bairro,numeroCasa,tipoConta,senha,saldo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(nome,CPF,dataNascimento,genero,telefone,cep,cidade,endereco,bairro,numeroCasa,tipoConta,senha,saldo))
            cur.connection.commit()
            return redirect('/')

class DeleteClienteController(MethodView):
    def post(self, id):
        with mysql.cursor()as cur:
            cur.execute("DELETE FROM clientes WHERE id =%s",(id))
            cur.connection.commit()
            return redirect('/')

class UpdateClienteController(MethodView):
    def get(self, id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM clientes WHERE id =%s",(id))
            cliente = cur.fetchone()
            return render_template('public/update.html', cliente=cliente)

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
            cur.execute("UPDATE clientes SET nome =%s,CPF =%s,dataNascimento =%s,genero =%s,telefone =%s,cep =%s,cidade =%s,endereco =%s,bairro =%s,numeroCasa =%s,tipoConta =%s,senha =%s WHERE  id = %s",(nome,CPF,dataNascimento,genero,telefone,cep,cidade,endereco,bairro,numeroCasa,tipoConta,senha,id))
            cur.connection.commit()
            return redirect('/')

class CadastroClienteController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM clientes")
            data = cur.fetchall()
            cur.execute("SELECT id FROM clientes ORDER BY id DESC LIMIT 1")
            numeroconta=cur.fetchone()
        return render_template('public/cadastro_cliente.html', data=data, numeroconta=numeroconta)

class LoginController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM clientes")
            data = cur.fetchall()
        return render_template('public/Login.html', data=data)

class LoginValicaoController(MethodView):
    def post(self):
        id=request.form['id']
        senhalogin = request.form['senha']

        with mysql.cursor() as cur:
            cur.execute("SELECT id FROM clientes WHERE id=%s",(id))
            cliente = cur.fetchone()
            if cliente!= None:
                cur.execute("SELECT * FROM clientes WHERE id =%s",(id))
                cliente = cur.fetchone()
                if senhalogin == cliente[12]:
                    cur.execute("SELECT * FROM clientes WHERE id =%s",(id))
                    cliente = cur.fetchone()
                    return render_template('public/home_user.html', cliente=cliente)
                else:
                    return "Tente Fazer o Login Novamente"
            else:
                return render_template('public/Login.html')

class HomeUserController(MethodView):
    def get(self, id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM clientes WHERE id =%s",(id))
            cliente = cur.fetchone()
        return render_template('public/home_user.html' , cliente=cliente)

class DadosController(MethodView):
    def get(self,id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM clientes WHERE id =%s",(id))
            cliente = cur.fetchone()
        return render_template('public/dados.html' , cliente=cliente)

class paginaDepositoController(MethodView):
    def get(self,id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM clientes WHERE id =%s",(id))
            cliente = cur.fetchone()
        return render_template('public/deposito.html', cliente=cliente)

class realizarDepositoController(MethodView):
    def post(self,id):
        deposito = float(request.form['deposito'])
               
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM clientes WHERE id =%s",(id))
            cliente = cur.fetchone()
            print ('o saldo atual; ',cliente[13])
            print ('tipo1',type(cliente[13]))
            print ('tipo2', type(deposito))
            saldofinal = deposito+cliente[13]
            cur.execute("UPDATE clientes SET saldo =%s WHERE  id = %s",(saldofinal,id))
            cur.connection.commit()
        return 'Deposito Realizado com Sucesso!!'

class paginaSaqueController(MethodView):
    def get(self,id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM clientes WHERE id =%s",(id))
            cliente = cur.fetchone()
        return render_template('public/saque.html', cliente=cliente)

class realizarSaqueController(MethodView):
    def post(self,id):
        saque = float(request.form['saque'])*(-1)
               
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM clientes WHERE id =%s",(id))
            cliente = cur.fetchone()
            print ('o saldo atual; ',cliente[13])
            print ('tipo1',type(cliente[13]))
            print ('tipo2', type(saque))
            print ('saque',saque)
            saldofinal = ((saque)+(cliente[13]))
            print ('O saldo final é:',saldofinal)
            cur.execute("UPDATE clientes SET saldo =%s WHERE  id = %s",(saldofinal,id))
            cur.connection.commit()
        return 'Saque Realizado com Sucesso!!!'
           

      
        
        
       
        
    
