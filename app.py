from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def view_home():
    return render_template("index.html", title="Home page")

@app.route("/aboutUs")
def view_aboutUs_page():
    return render_template("aboutUs.html", title="About Us")

@app.route("/second")
def view_second_page():
    return render_template("index.html", title="Second page")

if __name__ == '__main__':
    app.run(debug=True)