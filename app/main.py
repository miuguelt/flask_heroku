from flask import Flask, render_template
  
app = Flask(__name__) 
  
@app.route("/") 
def index(): 
    #return "<h1>Hola Formadores Sena!</h1>"
    return render_template("index.html")