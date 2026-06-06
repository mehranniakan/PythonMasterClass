from docutils.nodes import description
from flask import Flask, render_template, redirect, request, url_for
from kivy import level

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    full_name = 'مهران نیاکان'
    description  = """من یک توسعه دهنده جنگو در اهواز هستم و ویژگی هایی را ایجاد می کنم
     که بهترین هستند مناسب برای کار مورد نظر."""
    return render_template('index.html',context={
        'full_name': full_name,
        'description': description
    })

@app.route('/Skills')
def about():
    full_name = 'مهران نیاکان'
    description = """من یک توسعه دهنده جنگو در اهواز هستم و ویژگی هایی را ایجاد می کنم
     که بهترین هستند مناسب برای کار مورد نظر."""
    birthdate = "02.08.1374"
    age = 30
    address = 'اهواز - پادادشهر'
    email = 'mehran613.niakan@gmail.com'
    mobile = '09166230143'
    nat = 'ایرانی'
    ed = 'مهندسی نرم افزار - مهندسی عمران'
    level = 'جونیور'
    intrest = 'برنامه نویسی'

    skills = {
        'Python': 80,
        'php' : 80,
        'Django': 60,
        'Flutter': 40,
        'C': 20,
        'IOT' : 20
    }

    return render_template('about.html',context={
        'full_name': full_name,
        'description': description,
        'birthdate': birthdate,
        'age': age,
        'address': address,
        'email': email,
        'mobile': mobile,
        'nat': nat,
        'ed': ed,
        'level': level,
        'skills': skills,
        'intrest': intrest,
    })

@app.route('/Projects')
def portfolio():
    return render_template('portfolio.html')

if __name__ == '__main__':
    app.run(debug=True)