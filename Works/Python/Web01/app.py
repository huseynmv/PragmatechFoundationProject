from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

employee=[
    {
        'ad':'Huseyn',
        'soyad':'Mammadov',
        'email':'huseynmv@yahoo.com'
    },

    {
        'ad' : 'Saleh',
        'soyad' : 'Bayramaliyev',
        'email' : 'sbaa999@gmail.com'
    },
    {
        'ad' : 'Yusif',
        'soyad' : 'Osmanov',
        'email' : 'yusif@gmail.com'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/works')
def works():
    return render_template('works.html', employee=employee)

if __name__=="__main__" :
    app.run(debug=True) 