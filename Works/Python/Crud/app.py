from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
import random

app=Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///xeberdb.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db=SQLAlchemy(app)

class News(db.Model):
    news_id=db.Column(db.Integer, primary_key=True)
    news_title=db.Column(db.String(50))
    news_content=db.Column(db.String(255))
    news_date=db.Column(db.String(50))
    news_img=db.Column(db.String(100))

@app.route("/")
def index():
    xeberler=News.query.all()
    return render_template('index.html', news=xeberler)

@app.route("/admin")
def admin():
    xeberler=News.query.all()
    return render_template("admin.html",news=xeberler )


@app.route("/add", methods=['GET','POST'])
def add():
    if request.method=='POST':
        file = request.files['shekil']
        filename = secure_filename(file.filename)
        randomname = random.randint(1,1000)
        filename = str(randomname)+ '.' + filename.split('.')[1]
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        bashliq=request.form['bashliq']
        vaxt=request.form['vaxt']
        kontent=request.form['kontent']
        xeber=News(
            news_title=bashliq,
            news_content=kontent,
            news_date=vaxt,
            news_img=os.path.join(app.config['UPLOAD_FOLDER'], filename))
        db.session.add(xeber)
        db.session.commit()
        return redirect('/admin')
    return render_template("add.html")


@app.route("/delete/<int:id>")
def delete(id):
    xeber=News.query.filter_by(news_id=id).first()
    db.session.delete(xeber)
    db.session.commit()
    return redirect('/admin')


@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    news=News.query.filter_by(news_id=id).first()
    if request.method=='POST':
        news=News.query.filter_by(news_id=id).first()
        news.news_title=request.form['bashliq']
        news.news_vaxt=request.form['vaxt']
        news.news_content=request.form['kontent']
        db.session.commit()
        return redirect('/admin')
    return render_template('update.html', news=news)

@app.route("/show/<int:id>",methods=["GET","POST"] )
def show(id):
    xeber=News.query.filter_by(news_id=id).first()
    if xeber==id:
        return render_template("show.html", news=xeber)
    return render_template("show.html", news=xeber)

if __name__=='__main__':
    app.run(debug=True)