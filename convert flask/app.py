from flask import Flask,render_template,redirect,url_for,flash,request
from control import Yb
app = Flask(__name__,template_folder='templates')
app.secret_key = 'secreto'

@app.route('/')#,methods=['POST']
def Main():
    return render_template("main.html")

@app.route('/enviar',methods=['POST'])
def Enviar():
    try:
        if request.method == 'POST':
            url = request.form['url']
            opcion = request.form['opcion']
            con = Yb()
            con.Convert(url,opcion)
            flash(con.msj)
            return redirect(url_for("Main"))
    except:
        print ("error")

if __name__ == '__main__':
    app.run(port = 5000, debug = False)