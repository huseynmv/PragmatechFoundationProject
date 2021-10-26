from flask import Flask,render_template,request,redirect

class YeniXeber():
    def __init__ (self, _id, _title, _desc, _date, _content):
        self.id=_id
        self.bashliq=_title
        self.xulase=_desc
        self.vaxt=_date
        self.kontent=_content

news=[]

_id=1

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', news=news)

@app.route('/admin')
def admin():
    return render_template('admin.html', news=news)

@app.route("/add_news", methods=['GET', 'POST'])
def add_news():
    if request.method=='POST':
        global _id
        _bashliq=request.form['bashliq']
        _xulase=request.form['xulase']
        _vaxt=request.form['vaxt']
        _kontent=request.form['kontent']
        xeber=YeniXeber(_id, _bashliq, _xulase, _vaxt, _kontent)
        news.append(xeber)
        _id=_id+1
        return redirect('/admin')
    return render_template('add_news.html')


@app.route('/admin/delete_user/<id>')
def delete_user(id):
    for xeber in news :
        if xeber.id==int(id):
            news.remove(xeber)
            return redirect('/admin')
    return redirect('/admin')


@app.route("/admin/show/<id>")
def show(id):
    for xeber in news :
        if xeber.id==int(id):
            return render_template('show_news.html', news=news)
    return render_template('show_news.html')

@app.route("/admin/update_user/<id>", methods=['GET', 'POST'])
def update_news(id):
    if request.method=='POST':
        for xeber in news:
            _bashliq=request.form['bashliq']
            _xulase=request.form['xulase']
            _vaxt=request.form['vaxt']
            _kontent=request.form['kontent']
            for xeber in news :
                if xeber.id==int(id):
                    xeber.bashliq=_bashliq
                    xeber.xulase=_xulase
                    xeber.vaxt=_vaxt
                    xeber.kontent=_kontent
                    return redirect('/admin')

    for xeber in news:
        if xeber.id==int(id):
            return render_template('/update_user.html', xeber=xeber)
    return redirect('/admin')

if __name__=='__main__':
    app.run(debug=True)