USE biblioteca;

DROP TABLE IF EXISTS libri;

CREATE TABLE libri (
    Genere varchar(255),
    Titolo varchar(255),
    Autore varchar(255),
    CasaEditrice varchar(255),
    Anno int,
    Luogo varchar(255)
);

LOAD DATA INFILE '/var/lib/mysql-files/BIBLIOTECA.csv' 
INTO TABLE libri 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 2 ROWS;
