from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firstapp.db'
db = SQLAlchemy(app)

class FirstApp(db.Model):   
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(100), nullable=False)
    lname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    
    def __repr__(self):
        return f"{self.sno} - {self.fname}"

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        if fname and lname and email:
            firstapp = FirstApp(fname=fname, lname=lname, email=email)
            db.session.add(firstapp)
            db.session.commit()
            return redirect(url_for('hello_world'))

    allpeople = FirstApp.query.all()
    return render_template("index.html", allpeople=allpeople)
@app.route("/delete/<int:sno>")
def delete(sno):
    person = FirstApp.query.filter_by(sno=sno).first()
    db.session.delete(person)
    db.session.commit()
    return redirect("/")

@app.route("/update/<int:sno>")
def update(sno):
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        if fname and lname and email:
            person = FirstApp.query.filter_by(sno=sno).first()
            person.fname = fname
            person.lname = lname
            person.email = email
            db.session.add(person)
            db.session.commit()
    person = FirstApp.query.filter_by(sno=sno).first()
    return render_template("update.html", person=person)
if __name__ == "__main__":
    app.run(debug=True)
