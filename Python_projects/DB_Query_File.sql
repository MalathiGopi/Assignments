create database student_db;
use student_db;

create table student_table(
id int auto_increment primary key,
name varchar(50),
age int,
city varchar(50)
);

desc student_table;

select * from student_table;
insert into student_table(name,age,city) values("Niju",22,"TN");