from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app=Flask(__name__)

# MySQL Configuration
mysql_config = {
    'host': 'localhost',
    'user': 'root',       # Your MySQL username
    'password': 'xxxxx',   # Your MySQL password
    'database': 'student_db',       # Your MySQL database name
}

def db_exec(query):
    con = mysql.connector.connect(**mysql_config)
    cur=con.cursor()
    cur.execute(query)
    result = cur.fetchall()
    con.commit()
    cur.close()
    return result


@app.route('/')
def index():
    #display 
    res=db_exec("SELECT * FROM student_table")
    return render_template("index.html",result=res)

@app.route('/addstudent', methods=['POST'])
def add():
    if request.method == 'POST':
        name=request.form['name']
        age=request.form['age']
        city=request.form['city']
        print(name,age,city)
        #insert
        try:
            res=db_exec("Insert into student_table(name,age,city) values({},{},{})".format(name,age,city))
        except Exception as e:
            print("Something went wrong")
        return redirect(url_for("index"))

@app.route('/deletestudent/<int:id>')
def delete(id):
    #delete
    res=db_exec("DELETE FROM student_table WHERE id={}".format(id))
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)