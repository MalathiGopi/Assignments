from flask import Flask, render_template  #importing flask here
import mysql.connector

# class Database:
#     def __init__(self):
#         try:
#             print("constructor called to intialise the db config....")
#             self.user="root"
#             self.password="malu1234"
#             self.database="student_db"
#             self.host="localhost"
#             self.connection_object=mysql.connector.connect(user=self.user,password=self.password,database=self.database,host=self.host)
#             if self.connection_object.is_connected():
#                 self.db_Info = self.connection_object.get_server_info()
#                 self.cursor = self.connection_object.cursor()
#                 query="select*from student_table"
#                 self.cursor.execute(query)
#                 self.result=self.cursor.fetchall() 
#                 return self.result
#             else:
#                 print("OOps....Not connected ....!")
#         except Exception as e:
#             print("DB error : ",e)
#         finally:
#             if self.connection_object.is_connected():
#                 self.cursor.close()
#                 self.connection_object.close()
#                 print("MySQL connection is closed")
        


    # def execute_query(self):
    #     query="select*from student_table"
    #     self.cursor.execute(query)
    #     self.result=self.cursor.fetchall() 
    #     return self.result
    
app=Flask(__name__)   #create object

@app.route('/')     #decorator to override the route
def hello():
    return render_template("index.html")

@app.route('/student')
def show_data():
    connection_object=mysql.connector.connect(user="root",password="malu1234",database="student_db",host="localhost")
    if connection_object.is_connected():
        db_Info = connection_object.get_server_info()
        cursor = connection_object.cursor()
        query="select*from student_table"
        cursor.execute(query)
        res=cursor.fetchall() 
        print(res)
    return render_template("student.html",result=res)


if __name__ == "__main__": #initial point
    app.run(debug=True)    #triggereing the run