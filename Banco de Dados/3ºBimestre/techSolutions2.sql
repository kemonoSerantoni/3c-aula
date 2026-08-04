CREATE DATABASE IF NOT EXISTS techsolutions_a2;
USE techsolutions_a2;
CREATE TABLE fornecedores (
id_fornecedor INT AUTO_INCREMENT PRIMARY KEY,
razao_social varchar (100) NOT NULL,
cnpj VARCHAR (18) UNIQUE NOT NULL );

CREATE TABLE clientes (
id_cliente INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR (100) NOT NULL,
email VARCHAR (100) UNIQUE NOT NULL );


CREATE TABLE produtos (
id_produto INT AUTO_INCREMENT PRIMARY KEY,
nome_produto VARCHAR (100) NOT NULL,
preco DECIMAL (10, 2) NOT NULL,
id_fornecedor INT, 
foreign key (id_fornecedor) references fornecedores(id_fornecedor) 
);

CREATE TABLE vendas (
id_vendas INT AUTO_INCREMENT PRIMARY KEY,
id_cliente INT NOT NULL,
data_venda DATETIME DEFAULT CURRENT_TIMESTAMP,
foreign key (id_cliente) references clientes(id_cliente) 
);





