create database loja_pw;
use loja_pw;

create table PRODUTOS (
	id int primary key auto_increment,
    nome varchar(100),
    categoria varchar(50),
    preco decimal(10,2),
    data_venda date,
    estoque int
    );
    
INSERT INTO PRODUTOS (nome, categoria, preco, data_venda, estoque) VALUES
('Teclado Mecanico','Perifericos', 250.00, '2025/10/10', 15),
('Mouse Gamer','Perifericos', 120.00, '2026/01/05', 30),
('Monitor 24"','Monitores', 899.00, '2026/03/12', 8),
('Cadeira Office','Moveis', 1200.00, '2024/05/05', 5),
('Mousepad XL','Perifericos', 80.00, '2026/04/30', 15);

select * from PRODUTOS
WHERE categoria = 'Perifericos' AND preco > 100;

select * from PRODUTOS
WHERE estoque > '15' AND preco >= 50;

select * from PRODUTOS
WHERE nome = 'Mouse Gamer';

select * from PRODUTOS
WHERE nome LIKE '%Mouse%';

-- EXEMPLO 2: comendo LIKE
select * from PRODUTOS
WHERE nome LIKE '%Mouse%'
ORDER BY preco DESC;

select * from PRODUTOS
WHERE nome LIKE '%Mouse%'
ORDER BY preco ASC; 

-- EXEMPLO 3: Count()
select count(*) as total_perifericos
FROM produtos
WHERE categoria = 'Perifericos';





