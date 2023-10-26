import mysql.connector

class Database():
    def __init__(self):
        try:
            print("constructor called to intialise the db config....")
            self.user="root"
            self.password="xxxxx"
            self.database="student_db"
            self.host="localhost"
            self.connection_object=mysql.connector.connect(user=self.user,password=self.password,database=self.database,host=self.host)
            if self.connection_object.is_connected():
                self.db_Info = self.connection_object.get_server_info()
                self.cursor = self.connection_object.cursor()
            else:
                print("OOps....Not connected ....!")
        except Exception as e:
            print("DB error : ",e)
        finally:
            if self.connection_object.is_connected():
                self.cursor.close()
                self.connection_object.close()
                print("MySQL connection is closed")
        


    def execute_query(self,query):
        self.cursor.execute(query)
        self.result=self.cursor.fetchall() 
        self.data=[]       
        for item in self.result:
            print(item)
            self.data.append(item)
        return self.data
    