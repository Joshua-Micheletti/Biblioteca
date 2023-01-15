DROP DATABASE IF EXISTS biblioteca;

CREATE DATABASE biblioteca;

USE biblioteca;


DROP TABLE IF EXISTS libri;

CREATE TABLE libri (
    ID int NOT NULL AUTO_INCREMENT,
    Genere varchar(255),
    Titolo varchar(255),
    Autore varchar(255),
    CasaEditrice varchar(255),
    Anno int,
    Luogo varchar(255),
    PRIMARY KEY (ID)
);

LOAD DATA INFILE '/var/lib/mysql-files/BIBLIOTECA.csv' 
INTO TABLE libri 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 2 ROWS
(@col1, @col2, @col3, @col4, @col5, @col6)
SET Genere = @col1, Titolo = @col2, Autore = @col3, CasaEditrice = @col4, Anno = @col5, Luogo = @col6;



DROP TABLE IF EXISTS utenti;

CREATE TABLE utenti (
    Nome varchar(255) NOT NULL,
    Password varchar(255) NOT NULL,
    IDLibro int,
    PRIMARY KEY (Nome, Password),
    FOREIGN KEY (IDLibro) REFERENCES libri(ID)
);


DROP TABLE IF EXISTS restituzioni;

CREATE TABLE restituzioni (
    Nome varchar(255) NOT NULL,
    Password varchar(255) NOT NULL,
    IDLibro int NOT NULL,
    Voto int,
    Commento varchar(1023),
    PRIMARY KEY (Nome, Password, IDLibro),
    FOREIGN KEY (Nome, Password) REFERENCES utenti(Nome, Password),
    FOREIGN KEY (IDLibro) REFERENCES libri(ID)
);


# PROCEDURES
DELIMITER //

CREATE PROCEDURE GetAverageScore(IN ID int)
BEGIN
    SELECT AVG(Voto)
    FROM restituzioni
    WHERE IDLibro = ID;
END //

DELIMITER ;