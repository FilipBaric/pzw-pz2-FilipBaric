from flask import Flask, render_template, session, redirect,url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

apartmani = [
    {"id": 1, "naslov": "Apartman 1", "cijena": 3999},
    {"id": 2, "naslov": "Apartman 2", "cijena": 6999},
    {"id": 3, "naslov": "Apartman 3", "cijena": 8999}
]

app = Flask(__name__)
Bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = "TAJNIKLJUC"

class LoginForm(FlaskForm):
    name = StringField("Username")
    password = PasswordField("Password", validators= [DataRequired()])
    submit = SubmitField("Login")

@app.route("/")
def index():
    return render_template("index.html", name = session.get("name", None))

@app.route("/login.html", methods = ["POST", "GET"])
def login():
    name = None
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        form.name.data = ""
        return redirect(url_for("index"))
    return render_template("login.html", form = form, name = name)

@app.route('/signout.html')
def sign_out():
    session.pop('name')
    return redirect(url_for('index'))

@app.route("/galerija.html")
def galerija():
    return render_template("galerija.html")

@app.route("/pricing.html")
def pricing():
    return render_template("pricing.html", apartmani = apartmani)

@app.route("/checkout.html/<id>")
def checkout(id):
    apartman = [a for a in apartmani if a["id"] == int(id) ][0]
    return render_template("checkout.html", apartman = apartman)

@app.route("/zahvala.html")
def zahvala():
    return render_template("zahvala.html")

@app.route("/kontakti.html")
def kontakti():
    return render_template("kontakti.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"),500