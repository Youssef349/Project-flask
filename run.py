from flask import Flask, redirect, url_for, render_template, request, session, g, abort, \
     render_template, flash

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("layout.html", title = "Home")

if __name__== "__main__":
    app.run()