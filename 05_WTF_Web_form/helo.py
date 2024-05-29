from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Create a flask Instance 
app = Flask(__name__)

app.config['SECRET_KEY'] = "my super secret key is no one is supposed to no!"
# Create a Form Class
class NamerForm(FlaskForm):
      name = StringField("What's Your Name", validators=[DataRequired()])
      submit = SubmitField("Submit")


@app.route("/")
def hello():
    owner = "Rusaid!"
    
    return render_template("index.html",
                           first_name = owner,)


@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)

# Create Custom error  Pages

@app.errorhandler(404)
def page_not_found(e):
        return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
        return render_template("500.html"), 500



# Create Name Page
@app.route('/name', methods=['GET', 'POST'])
def name():
      name = None
      form = NamerForm()

      # Validate Form
      if form.validate_on_submit():
            name = form.name.data
            form.name.data = ''

      return render_template("name.html",
                             name = name,
                             form = form)



if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)