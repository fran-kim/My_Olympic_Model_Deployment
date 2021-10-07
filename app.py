from flask import Flask , render_template , request
import weight as w

app = Flask(__name__)

@app.route("/")
def render():    
    return render_template("index.html")

@app.route('/', methods=['POST'])
def pred():
    bw = request.form['bw']
    pred = w.lift_prediction(bw)
    return render_template("index.html", mylifts = pred)

    

#@app.route("/sub", methods = ['POST'])
#def submit():
    #HTML to Python file
#    if request.method == "POST":
#       name = request.form["username"]
#Python to HTML file
#    return render_template("sub.html", n = name)

if __name__ == "__main__":
    app.run(debug=True)
