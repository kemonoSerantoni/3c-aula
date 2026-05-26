CREATE DATABASE loja_limpeza;
USE loja_limpeza;

CREATE TABLE CLIENTE (
id int primary key auto_increment,
nome char(50) not null,
cpf varchar(14) not null,
cep varchar(10)
);


DROP TABLE FUNCIONARIO;
CREATE TABLE FUNCIONARIO (
id_funcionario int primary key auto_increment,
nome char(50) not null,
cpf varchar(14) not null,
funcao varchar(50) 
);

CREATE TABLE PRODUTO (
id_produto int primary key auto_increment,
tipo varchar(50) not null,
preco varchar(50) not null,
descricao varchar(50) not null
);

create table VENDAS (
id int primary key auto_increment not null,
    id_cliente int not null,
    numero_vendas varchar(100),
    data_venda date,
    estoque int,
    FOREIGN KEY (id_cliente) REFERENCES CLIENTE(id)
);


create table ESTOQUE (
id int primary key auto_increment not null,
    id_produto int not null,
    estoque_disponivel varchar(100),
    N_estoque int,
    FOREIGN KEY (id_produto) REFERENCES PRODUTO(id_produto)
);

create table Gerente (
id_gerente int primary key auto_increment not null,
nome VARCHAR(100),
cpf VARCHAR(14) UNIQUE,
email VARCHAR(100),
telefone VARCHAR(20),
data_contratacao DATE,
salario DECIMAL(10,2),
departamento VARCHAR(50),
status_ativo_inativo VARCHAR(20)
);

create table Fornecedor (
id_fornecedor int primary key auto_increment,
nome_empresa VARCHAR(100),
cnpj VARCHAR(18) UNIQUE,
telefone VARCHAR(20),
email VARCHAR(100),
endereco VARCHAR(150),
cidade VARCHAR(50),
estado VARCHAR(2),
cep VARCHAR(10),
representante VARCHAR(100),
status_ativo_inativo VARCHAR(20)
);
