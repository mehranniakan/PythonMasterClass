import uuid
from curses.ascii import isdigit

from fastapi import FastAPI, status, Body
from fastapi.responses import JSONResponse

app = FastAPI()

expenses = []


@app.get("/list")
def show_expenses():
    return JSONResponse({"expenses": expenses}, status_code=status.HTTP_200_OK)


@app.post("/create")
def create_expense(name: str = Body(), cost: int = Body()):
    if name and cost:
        expenses.append({
            "id": str(uuid.uuid4()),
            "name": name,
            "cost": cost
        })
        return JSONResponse(content={
            "Err": False,
            "Msg": "Item Created Successfuly"
        },
            status_code=status.HTTP_201_CREATED
        )
    else:
        return JSONResponse(content={
            "Err": True,
            "Msg": "Please Send Params"},
            status_code=status.HTTP_400_BAD_REQUEST
        )


@app.put("/update")
def edit_expense(id: str = Body(), name: str = Body(), cost: int = Body()):
    if id and name and cost:
        for item in expenses:
            if item["id"] == id:
                item["name"] = name
                item["cost"] = cost
                return JSONResponse(content={
                    "Err": False,
                    "Msg": "Item Updated Successfuly"
                }, status_code=status.HTTP_200_OK)
        else:
            return JSONResponse(content={
                "Err": True,
                "Msg": 'Nothing Found'
            }, status_code=status.HTTP_404_NOT_FOUND)
    else:
        return JSONResponse(content={
            "Err": True,
            "Msg": 'Please Send Params'
        }, status_code=status.HTTP_400_BAD_REQUEST)


@app.delete("/delete")
def delete_expense(id: str = Body()):
    if id:
        for item in expenses:
            if item["id"] == id:
                expenses.remove(item)
                return JSONResponse(content={
                    "Err": False,
                    "Msg": 'Item Deleted Successfuly'
                }, status_code=status.HTTP_204_NO_CONTENT)
        else:
            return JSONResponse(content={
                "Err": True,
                "Msg": 'Item Not Found'
            }, status_code=status.HTTP_404_NOT_FOUND)
    else:
        return JSONResponse(content={
            "Err": True,
            "Msg": 'Please Send Params'
        }, status_code=status.HTTP_400_BAD_REQUEST)


def get_single_expense(id: str):
    if id:
        for item in expenses:
            if item["id"] == id:
                return JSONResponse(content={
                    "Err": False,
                    "item": item
                }, status_code=status.HTTP_200_OK)
        else:
            return JSONResponse(content={
                "Err": True,
                "Msg": 'Item Not Found'
            }, status_code=status.HTTP_404_NOT_FOUND)
    else:
        return JSONResponse(content={
            "Err": True,
            "Msg": 'Please Send Params'
        },status_code=status.HTTP_400_BAD_REQUEST)


def item_filter(max_price:int):
    if max_price and isdigit(max_price):
        items = [item for item in expenses if item["cost"] <= max_price]
        return JSONResponse(content={
            "Err": False,
            'list': items,
        },status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content={
            "Err": True,
            "Msg": "Please Send Params"
        },status_code=status.HTTP_400_BAD_REQUEST)
