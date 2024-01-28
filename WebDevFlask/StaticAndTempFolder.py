from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():

    return render_template('index.html')

@app.route("/about")
def harry():
    name = "Harry"
    return render_template('about.html', name2 = name)   #name2 from about.html
app.run(debug=True)
