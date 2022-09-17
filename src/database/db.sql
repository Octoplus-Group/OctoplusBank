CREATE TABLE IF NOT EXISTS clientes(
    code int(5) UNSIGNED ZEROFILL NOT NULL,
    nome char(50) NOT NULL,
    CPF int(11),
    dataNascimento date,
    genero varchar(10),
    telefone int(20),
    cep int(8),
    endereco char(100),
    bairro char(50),
    numeroCasa int(5),
    tipoConta varchar(20),
    senha password(20),
    saldo decimal(20,2),
    primary key('code')
);



ALTER TABLE clientes ADD foreign key ('')