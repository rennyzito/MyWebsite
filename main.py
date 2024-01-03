from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from markupsafe import Markup

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/', methods=["GET", "POST"])
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False)
