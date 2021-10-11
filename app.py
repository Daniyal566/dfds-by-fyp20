from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')
@app.route("/contact")
def contact():
    return render_template('contact.html')
@app.route("/team")
def team():
    return render_template('team.html')
@app.route("/faq")
def faq():
    return render_template('faq.html')
@app.route("/blogs")
def blogs():
    return render_template('blogs.html')
@app.route("/login")
def login():
    return render_template('login.html')
@app.route("/register")
def register():
    return render_template('register.html')


app.run(debug=True)
if _name_ == "__main__":
    app.run(debug=True)