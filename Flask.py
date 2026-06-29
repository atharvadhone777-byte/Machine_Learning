from flask import Flask,render_template
app=Flask(__name__) #Initializes a flask app

#1.ROUTING 
@app.route('/post/<int:id>') #Only particular datatype hi input lega
def show_post(id):
    # Shows the post with given id.
    return f'This post has the id {id}'

@app.route('/user/<username>') #Use of variable
def show_user(username):
    # Greet the user
    return f'Hello {username} !'

@app.route("/hello")
def hello():
    return "Hello, Welcome to GeeksForGeeks"
  
@app.route("/")
def index():
    return "Homepage of GeeksForGeeks"

#2. Rendering documents of HTML
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<name>")
def welcome(name): #Passes variables
    return render_template("welcome.html", name=name)

#In HTML
# <a href="/home">Home</a>
# <a href="/">Index</a>
# we can join two pages link in one page
# Agar Home pe click karoge to home wale page pr chale jaoge
@app.route("/home")
def home():
    return render_template("home.html")

#FOR DEBUGGING ERROR
if __name__=='__main__':
    app.run()