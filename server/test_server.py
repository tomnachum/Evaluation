from fastapi.testclient import TestClient
from .server import app
import pytest
import json

client = TestClient(app)

# ----------------------------- Test Suite
# class TestAddPokemon:
# ----------------------------- Unit Test - make sure that the test doesn't affect the DB
#     def test_add_yanma(self):
#         response = client.post(
#             "/pokemons", json.dumps({"name": "yanma", "height": 100, "weight": 100})
#         ).json()
#         assert "yanma" in get_pokemons_by_type("bug")
#         assert "yanma" in get_pokemons_by_type("flying")
#         remove_pokemon_from_DB(get_pokemon_id("yanma"))


# class TestUpdatedPokemonTypes:
#     def test_venusaur(self):
#         client.get("/pokemons/venusaur").json()
#         assert "venusaur" in get_pokemons_by_type("poison")
#         assert "venusaur" in get_pokemons_by_type("grass")
