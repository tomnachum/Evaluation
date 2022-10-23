from fastapi import FastAPI, Request, Response, status
import uvicorn
import requests
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from utils.constants import *
from server_helper import *

app = FastAPI()

app.mount(
    f"/{JS_FILES_DIR}",
    StaticFiles(directory=JS_FILES_DIR),
    name=JS_FILES_DIR,
)

app.mount(
    f"/{TEMPLATE_DIR}",
    StaticFiles(directory=TEMPLATE_DIR),
    name=TEMPLATE_DIR,
)


@app.get("/")
def get_html():
    return FileResponse(HTML_DIR)


@app.get("/recipes", status_code=status.HTTP_200_OK)
async def get_recipes(response: Response, contains=None, dairy=False, gluten=False):
    if contains is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Error": {"details": "Query param 'contains' is mandatory."}}
    recipes = get_recipes_from_api(contains)
    if not recipes:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "Error": {"details": f"There are no recipes which contains '{contains}'"}
        }
    dairy = True if dairy == "True" else False
    gluten = True if gluten == "True" else False
    if dairy or gluten:
        recipes = filter_recipes_by_sensitivities(recipes, dairy, gluten)
    return {"total": len(recipes), f"recipes that contains {contains}": recipes}


# ----------------------------- a request with a body
# @app.put("/endpoint")
# async def add_player(request: Request):
#     body = await request.json()

# ----------------------------- external api call
# def external_api_call():
#     pokemon_response = requests.get(
#         f"https://pokeapi.co/api/v2/pokemon/{p_name}"
#     ).json()

# ----------------------------- status code
# @app.put("/get-or-create-task/{task_id}", status_code=status.HTTP_200_OK)
# def get_or_create_task(task_id: str, response: Response):
#     if task_id not in tasks:
#         tasks[task_id] = "This didn't exist before"
#         response.status_code = status.HTTP_201_CREATED
#     return tasks[task_id]

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8045, reload=True)
