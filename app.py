from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')


@app.route("/page/text")
def text():
    return render_template('page.html', text="Python Flask!")

app.run()