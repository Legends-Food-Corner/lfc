from flask import Flask, render_template, request

app = Flask(__name__)

appTheme = "light"

COUNTRIES = ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua And Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Cook Islands', 'Costa Rica', 'Cote D\'Ivoire (Ivory Coast)', 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Democratic Republic of the Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands', 'Faroe Islands', 'Fiji Islands', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia The', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey and Alderney', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Honduras', 'Hong Kong S.A.R.', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau S.A.R.', 'Macedonia', 'Madagascar',
             'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Man (Isle of)', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'North Korea', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory Occupied', 'Panama', 'Papua new Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn Island', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania', 'Russia', 'Rwanda', 'Saint Helena', 'Saint Kitts And Nevis', 'Saint Lucia', 'Saint Pierre and Miquelon', 'Saint Vincent And The Grenadines', 'Saint-Barthelemy', 'Saint-Martin (French part)', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Svalbard And Jan Mayen Islands', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'The Bahamas', 'Togo', 'Tokelau', 'Tonga', 'Trinidad And Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks And Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City State (Holy See)', 'Venezuela', 'Vietnam', 'Virgin Islands (British)', 'Virgin Islands (US)', 'Wallis And Futuna Islands', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']


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
    return render_template("settings/settings.htm", appTheme=appTheme, countries=COUNTRIES)


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
