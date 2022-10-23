import requests
from DB.queries.queries import get_dietary_restrictions


def get_recipes_from_api(contains):
    recipes_response = requests.get(
        f"https://recipes-goodness.herokuapp.com/recipes/{contains}"
    ).json()
    recipes = recipes_response["results"]
    return recipes


def to_lower_case(arr):
    return [e.lower() for e in arr]


def get_sensitivities(dairy, gluten):
    dietary_restrictions = []
    if dairy:
        dietary_restrictions += get_dietary_restrictions("dairy")
    if gluten:
        dietary_restrictions += get_dietary_restrictions("gluten")
    return dietary_restrictions


def is_allowed(recipe, dietary_restrictions):
    ingredients = " ".join(recipe["ingredients"]).split()
    ingredients, dietary_restrictions = to_lower_case(ingredients), to_lower_case(
        dietary_restrictions
    )
    return not any([ingredient in dietary_restrictions for ingredient in ingredients])


def filter_recipes_by_sensitivities(recipes, dairy, gluten):
    dietary_restrictions = get_sensitivities(dairy, gluten)
    if not dietary_restrictions:
        return recipes
    return list(
        filter(lambda recipe: is_allowed(recipe, dietary_restrictions), recipes)
    )
