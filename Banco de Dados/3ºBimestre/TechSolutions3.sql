CREATE DATABASE Techsolutions_a3;
USE techsolutions_a3;

CREATE TABLE CLIENTES (
id_cliente INT AUTO_INCREMENT PRIMARY KEY,
nome varchar (255),
email varchar (255),
cep varchar (255),
telefone varchar (50),
cpf varchar (11) );

CREATE TABLE PRODUTOS (
id_produto INT auto_increment PRIMARY KEY,
nome varchar (255),
descrição varchar (255),
preço decimal(10, 2) );

CREATE TABLE fornecedores (
id_fornecedor INT AUTO_INCREMENT PRIMARY KEY,
razao_social varchar (100) NOT NULL,
cnpj VARCHAR (18) UNIQUE NOT NULL );

CREATE TABLE vendas (
id_vendas INT AUTO_INCREMENT PRIMARY KEY,
id_cliente INT NOT NULL,
data_venda DATETIME DEFAULT CURRENT_TIMESTAMP,
foreign key (id_cliente) references clientes(id_cliente) 
);

CREATE TABLE ASSOCIATIVA (
id_associação INT PRIMARY KEY,
id_fornecedor INT NOT NULL,
id_vendas INT NOT NULL,


foreign key (id_fornecedor) references fornecedores(id_fornecedor),
foreign key (id_vendas) references vendas(id_vendas)
 );
