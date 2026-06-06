from dataclasses import dataclass
from uuid import uuid4
import os
import pandas as pd
from sanic import Request, json
from sanic.response import file
from sanic import Sanic, Request, json
from sanic_ext import Extend, openapi

app = Sanic("CookingApp")

Extend(app)

recipe_list = []


@dataclass
class AddRecipe:
    title: str
    category: str
    description: str
    estimate_time: int
    difficulty: str
    ingredients: list[str]


@dataclass
class UpdateRecipe:
    id: str
    title: str
    category: str
    description: str
    estimate_time: int
    difficulty: str
    ingredients: list[str]


@dataclass
class DeleteRecipe:
    id: str


@app.route("/recipes", methods=["GET"])
async def show_recipes(request: Request):
    return json({"recipes": recipe_list})


@app.route("/recipes", methods=["POST"])
@openapi.body(AddRecipe)
async def add_recipe(request: Request):
    data = request.json
    global recipe_list

    if data.get("title") and data.get("category") and data.get("description") and data.get("estimate_time") is not None:

        for item in recipe_list:
            if data.get("title") == item["title"]:

                return json({"Err": True, "Msg": "this recipe already exists"},
                            status=400)
        else:
            recipe_list.append({
                "id": str(uuid4()),
                "title": data["title"],
                "category": data["category"],
                "description": data["description"],
                "estimate_time": data["estimate_time"],
                "difficulty": data["difficulty"],
                "ingredients": data["ingredients"]
            })
            return json({"Err": False, "Msg": "Recipe added successfully"},
                        status=201)
    else:
        return json({"Err": True, "Msg": "title, category, description and estimate_time is required"},
                    status=400)


@app.route("/recipes", methods=["PUT"])
@openapi.body(UpdateRecipe)
async def update_recipe(request: Request):
    data = request.json
    global recipe_list

    if data.get("id"):
        if (data.get("title") and
                data.get("category") and
                data.get("description") and
                data.get("estimate_time") is not None):

            for item in recipe_list:
                if data["id"] == item["id"]:
                    item["title"] = data["title"]
                    item["category"] = data["category"]
                    item["description"] = data["description"]
                    item["estimate_time"] = data["estimate_time"]
                    item["difficulty"] = data["difficulty"]
                    item["ingredients"] = data["ingredients"]
                    return json({"Err": False, "Msg": "Recipe Updated successfully"},
                                status=200)

            else:
                return json({"Err": True, "Msg": "Recipe not found"},
                            status=404)

        else:
            return json({"Err": True, "Msg": "title, category, description and estimate_time is required"},
                        status=400)
    else:
        return json({"Err": True, "Msg": "Please send a recipe id"},
                    status=400)


@app.route("/recipes", methods=["DELETE"])
@openapi.body(DeleteRecipe)
async def delete_recipe(request: Request):
    data = request.json
    global recipe_list

    if data.get("id"):
        for item in recipe_list:
            if data["id"] == item["id"]:
                recipe_list.remove(item)
                return json({"Err": False, "Msg": "Recipe Removed successfully"},
                            status=204)
        else:
            return json({"Err": True, "Msg": "Recipe not found"},
                        status=404)
    else:
        return json({"Err": True, "Msg": "Please send a recipe id"},
                    status=400)


@app.route("/recipes", methods=["GET"])
async def export_csv(request: Request):
    global recipe_list

    if not recipe_list:
        return json({"Err": True, "Msg": "No recipes found"}, status=404)

    export_data = []
    for recipe in recipe_list:
        export_data.append({
            "id": recipe.get("id"),
            "title": recipe.get("title"),
            "category": recipe.get("category"),
            "description": recipe.get("description"),
            "estimate_time": recipe.get("estimate_time"),
            "difficulty": recipe.get("difficulty"),
            "ingredients": ", ".join(recipe.get("ingredients", []))
        })

    df = pd.DataFrame(export_data)

    filename = "recipes.csv"
    filepath = os.path.join(os.getcwd(), filename)

    df.to_csv(filepath, index=False, encoding="utf-8")

    return await file(
        filepath,
        filename=filename,
        mime_type="text/csv"
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8001, debug=True)
