from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index/index.htm")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('utilities/404page/404page.htm'), 404


if __name__ == "__main__":
    app.run(debug=True)
