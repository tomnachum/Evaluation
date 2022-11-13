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
    return {"recipes": recipes}


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
