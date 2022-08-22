from flask import Flask, render_template, request

app = Flask(__name__)

appTheme = "light"


@app.route("/")
def home():
    appTheme = request.cookies.get('app-theme')
    return render_template("home/home.htm", appTheme=appTheme)


@app.route("/login")
def login():
    appTheme = request.cookies.get('app-theme')
    return render_template("login/login.htm", appTheme=appTheme)


@app.route("/signup")
def signup():
    appTheme = request.cookies.get('app-theme')
    return render_template("signup/signup.htm", appTheme=appTheme)


@app.route("/careers")
def careers():
    appTheme = request.cookies.get('app-theme')
    return render_template("careers/careers.htm", appTheme=appTheme)


@app.route("/contact-us")
def contact_us():
    appTheme = request.cookies.get('app-theme')
    return render_template("contact-us/contact-us.htm", appTheme=appTheme)


@app.route("/settings")
def settings():
    appTheme = request.cookies.get('app-theme')
    return render_template("settings/settings.htm", appTheme=appTheme)


@app.route("/trending-dishes-all")
def trending_dishes_all():
    appTheme = request.cookies.get('app-theme')
    return render_template("trending-dishes-all/trending-dishes-all.htm", appTheme=appTheme)


@app.route("/trending-shops-all")
def trending_shops_all():
    appTheme = request.cookies.get('app-theme')
    return render_template("trending-shops-all/trending-shops-all.htm", appTheme=appTheme)


@app.route("/profile")
def profile():
    appTheme = request.cookies.get('app-theme')
    return render_template("profile/profile.htm", appTheme=appTheme)


@app.route("/help")
def help():
    appTheme = request.cookies.get('app-theme')
    return render_template("help/help.htm", appTheme=appTheme)


@app.route("/logout")
def logout():
    appTheme = request.cookies.get('app-theme')
    return render_template("login/login.htm", appTheme=appTheme)


@app.route("/menu")
def menu():
    appTheme = request.cookies.get('app-theme')
    return render_template("menu/menu.htm", appTheme=appTheme)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('utilities/404page/404page.htm'), 404


if __name__ == "__main__":
    app.run(debug=True)
