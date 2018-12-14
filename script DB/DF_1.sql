USE DB_Memoire;

-- creation d'une table qui illustre les dépendancesfonctionelles
--DROP TABLE TDependanceFonctionelle;

CREATE TABLE TDependanceFonctionelle (
    Professeur varchar(255),
    Classe varchar(255),
    Jour varchar(255),
    Heure varchar(255),
	--Matiere varchar(255),
	Eleves varchar(255),
);

INSERT INTO TDependanceFonctionelle VALUES ('Wijsen', 'A1', 'Lundi', '8h', 'BA1');
INSERT INTO TDependanceFonctionelle VALUES ('Wijsen', 'A1', 'Lundi', '8h', 'Anneé complémentaire');
INSERT INTO TDependanceFonctionelle VALUES ('Wijsen', 'A1', 'Lundi', '10h15', 'MA1');
INSERT INTO TDependanceFonctionelle VALUES ('GILLIS', 'A1', 'Lundi', '13h15', 'BA2' );
INSERT INTO TDependanceFonctionelle VALUES ('TUYTTENS', 'A1', 'Lundi', '15h30', 'BA2' );
--INSERT INTO TDependanceFonctionelle VALUES ('Buys', 'A1', 'Lundi', '8h15');
--INSERT INTO TDependanceFonctionelle VALUES ('Buys', 'A1', 'Lundi', '8h15');
--INSERT INTO TDependanceFonctionelle VALUES ('Buys', 'A1', 'Lundi', '8h15');
--INSERT INTO TDependanceFonctionelle VALUES ('Bruyere', 'A1', 'Lundi', '8h15');
--INSERT INTO TDependanceFonctionelle VALUES ('Bruyere', 'A1', 'Lundi', '8h15');

SELECT * FROM TDependanceFonctionelle;

-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------
USE DB_Memoire;

-- creation d'une table qui illustre les dépendancesfonctionelles
--DROP TABLE TDFnok;

CREATE TABLE TDFnok (
    id int,
    Facility varchar(255),
    Room int,
    Floor int,
	City varchar(255),
	Weight int,
);

INSERT INTO TDFnok VALUES (1, 'HQ', 322, 3, 'Paris', 3);
INSERT INTO TDFnok VALUES (2, 'HQ', 322, 30, 'Madrid', 1);
INSERT INTO TDFnok VALUES (3, 'HQ', 122, 1, 'Madrid', 1);
INSERT INTO TDFnok VALUES (4, 'Lab1', 835, 3, 'London', 4);

SELECT * FROM TDFnok;
-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------
USE DB_Memoire;

-- creation d'une table qui illustre les dépendancesfonctionelles
--DROP TABLE TDFnok;

CREATE TABLE TDFok (
    id int,
    Facility varchar(255),
    Room int,
    Floor int,
	City varchar(255),
);

INSERT INTO TDFok VALUES (1, 'HQ', 322, 30, 'Madrid');
INSERT INTO TDFok VALUES (2, 'HQ', 322, 30, 'Madrid');
INSERT INTO TDFok VALUES (3, 'HQ', 122, 1, 'Madrid');
INSERT INTO TDFok VALUES (4, 'Lab1', 835, 3, 'London');

SELECT * FROM TDFok;