from flask import Flask, render_template

# Create a flask Instance ()
app = Flask(__name__)

# http://127.0.0.1:5000/
# {{ url_for('hello') }}
@app.route("/")
def hello():
    owner = "Rusaid!"
    
    return render_template("index.html",
                           first_name = owner,)


# http://127.0.0.1:5000/user/Rusaid
# {{ url_for('user', name='rusaid') }}
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)

# Create Custom error  Pages

# Invalid URL
# http://127.0.0.1:5000/jj
@app.errorhandler(404)
def page_not_found(e):
        return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
        return render_template("500.html"), 500

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)