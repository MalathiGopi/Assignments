Create a CURD project : using command line I/O:
================================================

1)DB creation:
============
CREATE DATABASE student_db;

USE student_db;

CREATE TABLE users(
id int auto_increment primary key,
name varchar(50),
age int,
city varchar(50)
);

desc users;

select * from users;

insert into users(name,age,city) values("Niju",29,"palavilai");

2)$> pip install mysql-connector-python
======================================
install mysql connector - act as a intermediate between python and mysql DB

3)write program:
=================
connect DB
do CURD operations 
CHeck the cli
