CREATE DATABASE TechStore;
use TechStore;

DROP TABLE CLIENTES;
CREATE TABLE CLIENTES (
id_cliente int primary key auto_increment,
nome varchar(100),
datanasc date not null,
cep varchar(11),
email varchar(200),
cidade varchar(100),
telefone varchar(11)
);

CREATE TABLE PRODUTOS(
id_produto int primary key auto_increment,
nome varchar(100) not null,
descricao varchar(200),
preco decimal(10,2),
categoria varchar(100),
n_lote int not null
);

DROP TABLE CLIENTES;
DROP TABLE PRODUTOS;
DROP TABLE PEDIDOS;

CREATE TABLE PEDIDOS (
id_pedidos int primary key auto_increment,
id_cliente int not null,
id_produto int not null,
quantidade int not null,
FOREIGN KEY (id_cliente) REFERENCES CLIENTES(id_cliente),
FOREIGN KEY (id_produto) REFERENCES PRODUTOS(id_produto)
);
INSERT INTO CLIENTES (nome, datanasc, cep, email, cidade, telefone) VALUES 
('João Silva Santos', '1995-03-15', '01234-567', 'joao.silva@email.com', 'São Paulo', '(11) 98765-4321'),
('Maria Oliveira Costa', '1998-07-22', '22041-090', 'maria.oliveira@email.com', 'Rio de Janeiro', '(21) 99876-5432'),
('Pedro Henrique Almeida', '1993-11-08', '30123-456', 'pedro.almeida@email.com', 'Belo Horizonte', '(31) 91234-5678'),
('Ana Clara Ferreira', '2000-05-30', '01310-200', 'ana.ferreira@email.com', 'São Paulo', '(11) 94567-8901'),
('Lucas Mendes Rocha', '1996-09-12', '40000-000', 'lucas.mendes@email.com', 'Salvador', '(71) 98765-1234'),
('Beatriz Santos Lima', '1997-02-18', '04567-890', 'beatriz.lima@email.com', 'São Paulo', '(11) 92345-6789'),
('Rafael Costa Pereira', '1994-06-25', '51020-300', 'rafael.pereira@email.com', 'Recife', '(81) 95678-9012'),
('Laura Mendes Souza', '1999-10-03', '02030-000', 'laura.souza@email.com', 'São Paulo', '(11) 93456-7890'),
('Gabriel Oliveira Santos', '1992-12-14', '88040-000', 'gabriel.oliveira@email.com', 'Florianópolis', '(48) 97890-1234'),
('Isabela Ferreira Lima', '2001-04-27', '01505-010', 'isabela.ferreira@email.com', 'São Paulo', '(11) 96543-2109');


INSERT INTO PRODUTOS (nome, descricao, preco, categoria, n_lote) VALUES
('Smartphone Galaxy A15', 'Celular 4GB RAM 128GB armazenamento, tela 6.5 polegadas', 1299.90, 'Eletrônicos', 'LOTE-00123'),
('Notebook Dell Inspiron 15', 'Notebook Intel i5, 8GB RAM, 512GB SSD, Windows 11', 3299.00, 'Eletrônicos', 'LOTE-00124'),
('Teclado mecanico', 'Teclado mecanico, cores variadas', 499.90, 'Setup', 'LOTE-00567'),
('Galaxy Tab S10 Ultra e S11 Ultra', 'Tablet sansung, tecnologia de ponta', 1200.90, 'Eletrônicos', 'LOTE-00891'),
('Geladeira Frost Free 375L', 'Geladeira Brastemp 375 litros, branca', 2899.00, 'Eletrodomésticos', 'LOTE-00234'),
('Cadeira Gamer', 'cadeira', 900.90, 'gamer', 'LOTE-00745'),
('Mouse Red Dragon', 'mouse profissional', 159.90, 'mouses', 'LOTE-00389'),
('Mousepad', 'mouse pad vermelho', 42.50, 'eletronicos', 'LOTE-00912'),
('Fone de Ouvido Bluetooth', 'Fone sem fio com cancelamento de ruído', 229.90, 'Eletrônicos', 'LOTE-00156'),
('Conjunto setup', 'Conjunto com 5 peças, Cadeira, Mouse, PC montado, Teclado, Mousepad', 3899.90, 'Utensílios eletronicos', 'LOTE-00478');

INSERT INTO PEDIDOS (id_cliente, id_produto, quantidade) VALUES 
(1, 1, 1),     
(2, 3, 3),     
(3, 5, 1),     
(4, 2, 1),     
(5, 8, 2),     
(6, 4, 5),     
(7, 9, 1),     
(8, 6, 4),     
(9, 7, 2),     
(10, 10, 1),   
(3, 1, 1),     
(5, 3, 5),     
(1, 8, 3);     

SELECT * FROM CLIENTES;
SELECT * FROM PRODUTOS;
SELECT * FROM PEDIDOS;

SELECT * 
FROM CLIENTES 
WHERE cidade = 'São Paulo';

select * from PRODUTOS
WHERE nome LIKE '%Galaxy%';

select * from PRODUTOS
ORDER BY preco desc;

select count(*) as total_pedidos
FROM PEDIDOS;

SELECT cidade, COUNT(*) AS total_clientes
FROM CLIENTES 
GROUP BY cidade
ORDER BY total_clientes DESC;

SELECT * FROM PRODUTOS
	WHERE preco BETWEEN 200.00 AND 1000.00;	
    
SELECT SUM(preco) AS total_faturado
	FROM PRODUTOS;
    
SELECT AVG(preco) AS media_preco
	FROM PRODUTOS;

SELECT MAX(preco) AS maior_preco, MIN(preco) AS menor_preco FROM PRODUTOS;

    
    
	



