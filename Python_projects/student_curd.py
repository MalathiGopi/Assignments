from mysql import connector

def delete():
    print("Enter which id to delete")
    id=int(input("id to delete : "))
    query="delete from student_table where id={}".format(id)
    db_exec(query)
    select()

def update():
    name,age,city="name",1,"city"
    print("Enter some valus to update")
    id=int(input("Enter id to update : "))
    name=input("Enter name: ")
    age=int(input("Enter Age : "))
    city=input("Enter city: ")
    q="update student_table set name='{}',age={},city='{}' where id={}"
    query=q.format(name,age,city,id)
    db_exec(query)
    select()

def insert():
    print("Enter values : \n")
    name=input("Enter name: ")
    age=int(input("Enter Age : "))
    city=input("Enter city: ")
    query="insert into student_table(name,age,city) values ('{}',{},'{}')"
    fquery=query.format(name,age,city)
    db_exec(fquery)
    select()

def select():
    query="select * from student_table"
    db_exec(query)
 
def db_exec(query):
    try:
        connection_object=connector.connect(host='localhost',user='root',password='xxxxx',database='student_db')
        cursor_obj=connection_object.cursor()
        cursor_obj.execute(query)
        data=cursor_obj.fetchall()
        connection_object.commit()
        for i in data:
            print(i)
    except Exception as e:
        print("Something went wrong with db : ",e)
    finally:
        connection_object.close()

def choice():
    while True:
        print("Enter choice")
        print("1.select\n2.insert\n3.update\n4.delete\n5.exit")
        choice_num=int(input("Enter your choice : "))
        if choice_num == 1:
            select()
        elif choice_num ==2:
            insert()
        elif choice_num == 3:
            update()
        elif choice_num == 4:
            delete()
        elif choice_num == 5:
            break
        else:
            print("Enter correct number ")


def main():
    choice()

if __name__ == '__main__':
    main()