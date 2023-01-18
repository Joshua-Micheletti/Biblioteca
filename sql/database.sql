DROP DATABASE IF EXISTS Biblioteca;
CREATE DATABASE Biblioteca;
USE Biblioteca;


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


DROP TABLE IF EXISTS utenti;

CREATE TABLE utenti (
    Nome varchar(255) NOT NULL,
    Password varchar(255) NOT NULL,
    IDLibro int,
    PRIMARY KEY (Nome, Password),
    FOREIGN KEY (IDLibro) REFERENCES libri(ID) ON DELETE SET DEFAULT
);


DROP TABLE IF EXISTS restituzioni;

CREATE TABLE restituzioni (
    Nome varchar(255) NOT NULL,
    Password varchar(255) NOT NULL,
    IDLibro int NOT NULL,
    Voto int,
    Commento varchar(1023),
    CHECK (Voto >= 0 AND Voto <= 5),
    PRIMARY KEY (Nome, Password, IDLibro),
    FOREIGN KEY (Nome, Password) REFERENCES utenti(Nome, Password) ON DELETE CASCADE,
    FOREIGN KEY (IDLibro) REFERENCES libri(ID) ON DELETE CASCADE
);



LOAD DATA INFILE '/var/lib/mysql-files/BIBLIOTECA.csv' 
INTO TABLE libri 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 2 ROWS
(@col1, @col2, @col3, @col4, @col5, @col6)
SET Genere = @col1, Titolo = @col2, Autore = @col3, CasaEditrice = @col4, Anno = @col5, Luogo = @col6;



# PROCEDURES
DELIMITER //

CREATE PROCEDURE aggiungiUtente(IN inNome varchar(255), IN inPassword varchar(255))
BEGIN
    INSERT INTO utenti(Nome, Password)
    VALUES (inNome, inPassword);
END //


CREATE PROCEDURE rimuoviUtente(IN inNome varchar(255), IN inPassword varchar(255))
BEGIN
    DELETE FROM utenti
    WHERE Nome = inNome AND Password = inPassword;
END //


CREATE PROCEDURE votoMedio(IN inID int)
BEGIN
    SELECT AVG(Voto)
    FROM restituzioni
    WHERE IDLibro = inID;
END //


CREATE PROCEDURE rimuoviLibro(IN inID int)
BEGIN
    DELETE FROM libri
    WHERE ID = inID;
END //


CREATE PROCEDURE aggiungiLibro(IN inGenere varchar(255), IN inTitolo varchar(255), IN inAutore varchar(255), IN inCasaEditrice varchar(255), IN inAnno int, IN inLuogo varchar(255))
BEGIN
    INSERT INTO libri(Genere, Titolo, Autore, CasaEditrice, Anno, Luogo)
    VALUES (inGenere, inTitolo, inAutore, inCasaEditrice, inAnno, inLuogo);
END //


CREATE PROCEDURE prendiLibro(IN inID int, IN inNome varchar(255), IN inPassword varchar(255))
BEGIN
    IF (SELECT EXISTS( SELECT * FROM utenti WHERE Nome = inNome AND Password = inPassword AND IDLibro IS NULL)) THEN
        IF (SELECT NOT EXISTS( SELECT * FROM utenti WHERE IDLibro = inID)) THEN
            UPDATE utenti
            SET IDLibro = inID
            WHERE Nome = inNome AND Password = inPassword;
        END IF;
    END IF;
END //


CREATE PROCEDURE restituisciLibro(IN inID int, IN inNome varchar(255), IN inPassword varchar(255), IN inVoto int, IN inCommento varchar(255))
BEGIN
    IF (SELECT EXISTS( SELECT * FROM utenti WHERE Nome = inNome AND Password = inPassword AND IDLibro = inID)) THEN
        IF (SELECT EXISTS( SELECT * FROM restituzioni WHERE Nome = inNome AND Password = inPassword AND IDLibro = inID )) THEN
            UPDATE restituzioni
            SET Voto = inVoto, Commento = inCommento
            WHERE Nome = inNome AND Password = inPassword AND IDLibro = inID;

        ELSE
            INSERT INTO restituzioni(Nome, Password, IDLibro, Voto, Commento)
            VALUES (inNome, inPassword, inID, inVoto, inCommento);

        END IF;

        UPDATE utenti
        SET IDLibro = NULL
        WHERE Nome = inNome AND Password = inPassword;

    END IF;

END //



DELIMITER ;