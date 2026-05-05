create database floricultura;
use floricultura;

create table funcionario(
id_funcionario int primary key auto_increment,
nome_funcionario char(100) not null,
idade_funcionario int(3) not null,
email_funcionario varchar(100) not null,
telefone_funcionario varchar(17) not null,
cpf_funcionario varchar(14) not null,
endereço_funcionario varchar(100) not null,
cargo_funcionario char(30),
salario_funcionario varchar(30)
);

create table cliete(
id_cliente int primary key auto_increment,
nome_cliente char(100) not null,
email_cliente varchar(100) not null,
telefone_cliente varchar(17) not null,
cpf_cliente varchar(14) not null,
endereço_cliente varchar(100) not null
);

create table produto(
id_produto int primary key auto_increment,
preço_produto varchar(30) not null,
n_serie int(20) not null,
tipo_produto text(30) not null,
nome_produto varchar(100) not null,
cor_produto varchar(10) not null,
descrição_produto varchar(100) not null
);

