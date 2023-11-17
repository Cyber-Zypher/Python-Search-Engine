
# Search Engine with Python and MySQL
A simple Search engine program with Python and MySQL database with TKinter GUI.
Easily customizable with flexible syntax.

## Create Database and Tables
Simply run the ```firstrun.py``` script for autoconfiguring the database.
(Make sure to edit the user and password in every script before actually running the program.)

(or)

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

## File Structure.
Make Sure that the Files are stored as it is shown below.
```
Python_search_engine/
│
├── templates/
│   ├── add_results.html
│   ├── index.html
│   └── search_results.html
├── static/
│   └── styles.css
├── README.md
├── app.py
├── venv/       (virtual environment - recommended)
└── ...

```
## Authors

- [@sidharth_everett](https://github.com/Cyber-Zypher)
