create database bdbrasil;
use bdbrasil;

CREATE TABLE cliente(
cpf_cliente VARCHAR(11),
nome_cliente VARCHAR(20),
rua_cliente VARCHAR(30),
cidade_cliente VARCHAR(30),
estado_cliente VARCHAR(20),
rg_cliente VARCHAR(7),
idade_cliente INT,
data_cadastro DATE,
PRIMARY KEY (cpf_cliente)
);

CREATE TABLE agencia(
codigo_agencia INT,
nome_agencia char(15) not null,
cidade_agencia VARCHAR(40),
fundos numeric(10,2) DEFAULT 0,
PRIMARY KEY (codigo_agencia),
CHECK (fundos >=20)
);

CREATE TABLE emprestimo(
numero_emprestimo INT NOT NULL,
codigo_agencia INT NOT NULL,
total numeric(10,2),
PRIMARY KEY(numero_emprestimo),
FOREIGN KEY (codigo_agencia) references agencia(codigo_agencia),
CHECK (total > 0)
);

CREATE TABLE devedor(
cpf_cliente VARCHAR(11) not null,
numero_emprestimo int not null,
PRIMARY KEY (cpf_cliente, numero_emprestimo),
FOREIGN KEY (cpf_cliente) REFERENCES cliente(cpf_cliente),
FOREIGN KEY (numero_emprestimo) REFERENCES emprestimo(numero_emprestimo)
);