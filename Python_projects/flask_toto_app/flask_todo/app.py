from flask import Flask  #importing flask here

app=Flask(__name__)   #create object

@app.route('/')     #decorator to override the route
def hello():
    return "Hello.....guys"

if __name__ == "__main__": #initial point
    app.run(debug=True)    #triggereing the run