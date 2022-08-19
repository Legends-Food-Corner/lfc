from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home/home.htm")


@app.route("/login")
def login():
    return render_template("login/login.htm")


@app.route("/signup")
def signup():
    return render_template("signup/signup.htm")


@app.route("/careers")
def careers():
    return render_template("careers/careers.htm")


@app.route("/contact-us")
def contact_us():
    return render_template("contact-us/contact-us.htm")


@app.route("/settings")
def settings():
    return render_template("settings/settings.htm")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('utilities/404page/404page.htm'), 404


if __name__ == "__main__":
    app.run(debug=True)
