from sanic import Sanic, Request, json, exceptions
from sanic_ext import Extend, openapi
from uuid import uuid4

app = Sanic("ToDoApp")

Extend(app)

todo_list = []

class TaskBodyUpdate:
    id:str
    title:str
    description:str

class TaskBodyCreate:
    title:str
    description:str

class TaskBodyDelete:
    title:str
    description:str

@app.get("/list")
async def show_list(request : Request):
    global todo_list
    json_data = {"list": todo_list}
    return json(json_data, status=200)


@app.route("/create", methods=["POST"])
@openapi.body(TaskBodyCreate)
async def create(request):
    global todo_list
    data = request.json
    todo_list.append({
        'id': str(uuid4()),
        'title': data.get('title'),
        'description': data.get('description'),
    })
    return json({"success": True}, status=201)


@app.post("/update")
@openapi.body(TaskBodyUpdate)
async def update(request):

    global todo_list
    data = request.json

    for item in todo_list:
        if item['id'] == str(data.get('id')):

            if data.get('title') and data.get('description'):
                item['title'] = data.get('title')
                item['description'] = data.get('description')
            else:
                raise exceptions.BadRequest('Please provide title and description')

            return json({'message': 'Task Update Successfuly'}, status=200)
    else:
        raise exceptions.NotFound()


@app.post('/delete')
@openapi.body(TaskBodyDelete)
async def delete(request):
    global todo_list
    data = request.json
    if data.get('id'):
        todo_list = [task for task in todo_list if task['id'] != data.get['id']]
        return json({'success': True}, status=200)
    else:
        raise exceptions.NotFound()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True, auto_reload=True)