from flask import Flask, render_template

# Create a flask Instance ()
app = Flask(__name__)

""" # Create a route decorator
@app.route("/")
def hello():
    return "<h1>Hello World!</h1>" 
 """

@app.route("/")
def hello():
    return render_template("index.html")


# http://127.0.0.1:5000/user/Rusaid
@app.route('/user/<name>')
def user(name):
    return "<h1>Hello {}!</h1>".format(name)


if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)