from flask import Flask, render_template  #importing flask here
from db_exec import Database
app=Flask(__name__)   #create object

@app.route('/')     #decorator to override the route
def hello():
    return render_template("index.html")
@app.route('/student')
def show_data():
    def db_query():
        db_obj=Database()
        query="select*from student_table"
        output=db_obj.execute_query(query)
        print(output)
    res=db_query()
    return render_template("index.html",output=res)


if __name__ == "__main__": #initial point
    app.run(debug=True)    #triggereing the run