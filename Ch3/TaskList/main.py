import pandas as pd
from flask import Flask, render_template, request,redirect
from uuid import uuid4


tasks = []
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', tasks=None)


@app.route('/upload', methods=['POST'])
def upload():
    global tasks
    if 'file' not in request.files:
        return "فایلی انتخاب نشده است", 400

    file = request.files['file']

    try:
        df = pd.read_excel(file)
        df.columns = df.columns.str.strip()
        df.rename(columns={'عنوان وظیفه': 'title', 'توضیحات': 'description', 'وضعیت': 'status'}, inplace=True)
        df['id'] = [str(uuid4()) for _ in range(len(df))]
        tasks = df.to_dict(orient='records')
        return render_template('index.html', tasks=tasks)

    except Exception as e:
        return f"خطا در پردازش فایل: {e}"

@app.route('/add', methods=['POST'])
def add_task():
    global tasks
    if request.form.get('title') and request.form.get('description') and request.form.get('status'):

        tasks.append({
            'title': request.form.get('title'),
            'description': request.form.get('description'),
            'status': request.form.get('status')
        })

        return render_template('index.html', tasks=tasks)
    else:
        pass

@app.route('/edit/<task_id>', methods=['POST','GET'])
def edit_task(task_id):
    global tasks

    if request.method == 'GET':

        finded_task = None
        for item in tasks:
            if item['id'] == task_id:
                finded_task = item
                break

        if finded_task is None:
            return render_template('index.html', tasks=tasks)
        else:
            return render_template('edit.html', task=finded_task)

    elif request.method == 'POST':


        if (request.form.get('title') and
                request.form.get('description') and
                request.form.get('status') and
                task_id
        ):

            for item in tasks:
                if item['id'] == task_id:
                    item['title'] = request.form.get('title')
                    item['description'] = request.form.get('description')
                    item['status'] = request.form.get('status')
                    return render_template('index.html', tasks=tasks)
            else:
                return render_template('index.html', tasks=tasks)

@app.route('/delete/<task_id>', methods=['GET'])
def delete_task(task_id):
    global tasks

    if task_id :
        for item in tasks:
            if item['id'] == task_id:
                tasks.remove(item)
                return render_template('index.html', tasks=tasks)
        else:
            return render_template('index.html', tasks=tasks)
    else:
        return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
