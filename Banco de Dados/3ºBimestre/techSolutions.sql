CREATE DATABASE techsolutions_a1;
USE techsolutions_a1;
CREATE TABLE CLIENTES 
(id_clientes INT auto_increment primary key, 
nome VARCHAR (100) NOT NULL,
email VARCHAR (100) UNIQUE NOT NULL,
telefone VARCHAR (20) );

CREATE TABLE PRODUTOS
(id_produto INT AUTO_INCREMENT PRIMARY KEY,
nome_produto VARCHAR (100) NOT NULL,
preco DECIMAL (10,2) NOT NULL );

CREATE TABLE VENDAS
(id_vendas INT AUTO_INCREMENT PRIMARY KEY,
id_cliente INT NOT NULL,
id_produto INT NOT NULL,
data_venda DATE NOT NULL,
quantidade INT NOT NULL,
foreign key (id_cliente) references CLIENTES(id_clientes),
foreign key (id_produto) references PRODUTOS(id_produto) );

