from flask import Flask, render_template


# flask instance
app = Flask(__name__)

# Create route decoratry
@app.route('/')
#def index():
#    return "<h1> Hello World!! </h1>"
def index():
    return render_template("index.html")

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)

#create erorr pages 

#invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# internal server Erorr lol
@app.errorhandler(500)
def page_not_found(e):
    return render_template("505-html"), 500
