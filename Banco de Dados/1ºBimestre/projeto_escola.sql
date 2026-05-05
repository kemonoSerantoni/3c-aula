CREATE database escola_XZ;
use escola_XZ;

create table aluno(
id_aluno int primary key auto_increment,
nome varchar(50) not null
);

alter table aluno add column sobrenome varchar(50) not null;

select * from aluno;	
INSERT INTO alunos (nome, sobrenome) VALUES
('Lucas', 'Silva'),
('Maria', 'Oliveira'),
('João', 'Souza'),
('Ana', 'Costa'),
('Pedro', 'Santos'),
('Carla', 'Ferreira'),
('Rafael', 'Almeida'),
('Juliana', 'Pereira'),
('Bruno', 'Rodrigues'),
('Fernanda', 'Lima'),
('Diego', 'Gomes'),
('Patricia', 'Martins'),
('Felipe', 'Rocha'),
('Camila', 'Barbosa'),
('Gustavo', 'Ribeiro'),
('Larissa', 'Cardoso'),
('Thiago', 'Teixeira'),
('Aline', 'Correia'),
('Vinicius', 'Mendes'),
('Beatriz', 'Nunes');
update aluno set nome = "Nathan" where id_aluno = 14;
update aluno set nome = "Bruno" where id_aluno = 8;
update aluno set nome = "Feliz" where id_aluno = 15;
update aluno set nome = "moranguet" where id_aluno = 11;
update aluno set sobrenome = "Limão" where id_aluno = 19;

delete from aluno where id_aluno = 20;
delete from aluno where id_aluno = 7;
delete from aluno where id_aluno = 13;

insert into aluno (nome, sobrenome) values ("Teko", "minakama");

