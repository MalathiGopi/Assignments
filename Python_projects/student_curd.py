import mysql.connector

connection_object = mysql.connector.connect(host="localhost",username="root",password="xxxxxx",database="student_db")

# if connection_object:
#     print("connection success")
# else:
#     print("connnection fail")

def insert(name, age, city):
    pass

def update():
    pass

def select():
    pass

def delete():
    pass

while True:
    print("Hello choose your choice !!!! play with DB data")
    print("Enter your choice \n 1.insert data\n 2.update data\n 3.select data\n 4.delete data")
    choice = int(input("Enter your choice : "))
    if choice ==1:
        name = input()