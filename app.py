from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')


@app.route("/page/text")
def pageText():
    return render_template('page.html', text="Python Flask!")


@app.route("/form")
def formPage():
    return render_template('form.html')

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form['name']
    email = request.form['email']

    print("name",name)
    print("email",email)
    return redirect(url_for('success', name=name , action = "post"))

@app.route("/success/<action>/<name>")
def success(action,name):
    return  f"{action} : welcome {name}"

app.run()