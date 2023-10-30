Title : Login and Registration demo app in flask

Create Virtual Env : python -m venv flask_login

activate the Venv: cd flask_login/Scripts/ => ./activate

Install the below modules:
---------------------------

pip install flask flask-mysqldb

Create a DB using the below Query:
==================================

Create a Database: CREATE DATABASE IF NOT EXISTS flasklogin;

use the Database : USE flasklogin;

Create tables with fields id(primary key - int), username(varchar), password(varchar), email(varchar)

CREATE TABLE IF NOT EXISTS useraccounts(
    id int PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50)  NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL
    );
    
See the structure : DESC useraccounts;
