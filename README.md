# Progetto Basi di Dati
## Joshua Micheletti
## Matricola: 283057

## Database

Il progetto consiste nella creazione di un database in cui sono presenti informazioni su libri di una biblioteca casalinga, utenti che hanno accesso alla biblioteca e possono prendere in prestito e restituire i libri disponibili. Ad ogni restituzione, l'utente rilascia una recensione sul libro restituito.

Il database è implementato da uno script SQL **database.sql** all'interno della directory **sql** che crea la struttura del database, importa i dati dei libri dal file **BIBLIOTECA.csv** (posizionata correttamente relativa a MySQL, lo script SQL fornito funziona per ubuntu 20.04) e definisce delle procedure per lavorare con i dati.

Un database già implementato è hostato presso:

- host: solidgallium.ddns.net
- porta: 3306
- username: josh
- password: password
- database: Biblioteca


Altrimenti se si vuole implementare il database su una nuova macchina, basta utilizzare lo script fornito (**database.sql**) facendo attenzione di posizionare il file **BIBLIOTECA.csv** presso */var/lib/mysql-files/BIBLIOTECA.csv* (Ubuntu 20.04)


## Client

Il client il cui sorgente è situato in **src** è un programma in Python che automaticamente si collega al database presso l'IP *solidgallium.ddns.net*.

Se si vuole cambiare il database di riferimento, bisogna modificare i parametri del nuovo database nel file **src/globalVars.py**:

```sh
mydb = mysql.connector.connect(
    host = "solidgallium.ddns.net", # database IP (default port 3306)
    user = "josh",                  # username
    password = "password",          # password
    database = "Biblioteca"         # database to use
)
```


### Dipendenze:

- Python 3
- tkinter
- ttkthemes
- mysql-connector-python

### Installazione

In **install** sono forniti due script di installazione, uno per Windows e uno per Ubuntu 20.04

### Windows

Per installare il client, bisogna inizialmente installare Python 3 dal Microsoft Store (nel caso non sia già installato, aprendo un terminale e digitando *python*, verrà aperta automaticamente la pagina per installare l'ultima versione di Python 3)

Successivamente basta eseguire lo script **install/installWindows.bat** per installare le dipendenze del client e creare uno script **launch.bat** per eseguire il programma


### Ubuntu 20.04

Per installare il client basta eseguire lo script **install/installUbuntu.sh** (potrebbe essere necessario rendere lo script eseguibile, in tal caso, basta eseguire il comando *chmod +x <directory/dello/script/installUbuntu.sh> e successivamente eseguirlo)

Lo script installerà tutte le dipendenze necessarie e creerà uno script launch.sh per eseguire il programma


