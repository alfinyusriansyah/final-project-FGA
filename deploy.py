from flask import Flask, render_template,request
import ml as m

app = Flask(__name__)

@app.route('/', methods=["GET"])
def ping():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def submite():
    if request.method == "POST":
        th = request.form['year']
        mil = request.form['mileage']
        tx = request.form['tax']
        pg = request.form['mpg']
        engine = request.form['engine']
        predik = m.mark_predict(th,mil,tx,pg,engine)
        mks = predik

    return render_template("index.html", harga= mks)    

# @app.route("/sub", methods=['POST'])
# def submite():
#     if request.method == "POST":
#         name = request.form['model']

#     return render_template("sub.html", mod = name)

if __name__=='__main__':
    app.run(debug=True)
