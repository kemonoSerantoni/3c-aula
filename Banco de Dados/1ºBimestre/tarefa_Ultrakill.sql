create database Empresa_PWY;
use Empresa_PWY;

create table FUNCIONARIO(
id_funcionario int auto_increment not null,
cpf char(20) not null,
nome char(50) not null,
data_nasc date not null,
id_função int not null,
FOREIGN KEY (id_função) REFERENCES FUNÇÃO(id_função),
PRIMARY KEY (id_funcionario));

create table DEPARTAMENTO(
id_departamento int auto_increment not null,
nome char(40),
id_funcionario int not null,
PRIMARY KEY (id_departamento),
FOREIGN KEY (id_funcionario) REFERENCES FUNCIONARIO(id_funcionario));

create table FUNÇÃO(
id_função int(20) not null auto_increment,
nome char(40) not null,
PRIMARY KEY (id_função));

create table PRODUTO(
id_prod int not null auto_increment,
nome char not null,
descrição varchar(50) not null,
primary key (id_prod));

select * from FUNCIONARIO;
INSERT into FUNCIONARIO (cpf, nome, data_nasc) values
('101010101', 'joâo', '10/12/2009');