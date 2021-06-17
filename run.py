import os  # imports OS from the standard Python library
from flask import Flask, render_template  # imports Flask class from flask

app = Flask (__name__)  # Stores flask in a variable called app


@app.route("/")  # Route decorator tells flask what URL/file to access
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":  # Runs app with the following arguments. 
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
        """
        Allows debugging during development.
        Always set to false before submitting
        """