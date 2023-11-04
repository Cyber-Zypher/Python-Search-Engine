
# Search Engine with Python and MySQL
A simple Search engine program with Python and MySQL database with TKinter GUI.
Easily customizable with flexible syntax.

## Create Database and Tables
Open MySQL Commandline client and log in.

```
CREATE DATABASE SEARCH_ENGINE;
USE SEARCH_ENGINE;
CREATE TABLE search_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    keyword VARCHAR(255),
    result_text TEXT
);
```

## Install the required Libraries.

Clone the project

```
pip install mysql.connector
pip install Flask
```
or
```
python -m pip install mysql.connector
python -m pip install Flask
```
## Authors

- [@sidharth_everett](https://github.com/Cyber-Zypher)
