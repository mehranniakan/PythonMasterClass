import pandas as pd
from flask import Flask, render_template, request,redirect
from uuid import uuid4


hobbys = []
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    global hobbys
    return render_template('index.html', hobbys=hobbys)

@app.route('/add', methods=['POST','GET'])
def add_task():
    global hobbys

    if request.method == 'GET':
        return render_template('add_hobby.html')
    elif request.method == 'POST':
        if (request.form.get('name') and
                request.form.get('age') and
                request.form.get('interest') and
                request.form.get('interest_level')):

            if request.form.get('age').isdigit():

                hobbys.append({
                    'id': str(uuid4()),
                    'name': request.form.get('name'),
                    'age': request.form.get('age'),
                    'hobby': request.form.get('interest'),
                    'level': request.form.get('interest_level'),
                    'description': request.form.get('description'),
                })
            else:
                message = 'لطفا سن را به عدد وارد کنید !'
                return render_template('add_hobby.html', message=message)

            return render_template('index.html', hobbys=hobbys)
        else:
            message = 'لطفا تمامی فیلد هارا پر کنید . توضیحات اختیاری است  !'
            return render_template('add_hobby.html', message=message)
    else:
        return render_template('index.html', hobbys=hobbys)


if __name__ == '__main__':
    app.run(debug=True)
