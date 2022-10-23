import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="recipes_app",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor,
)


def get_dietary_restrictions(sensitivity):
    try:
        with connection.cursor() as cursor:
            query = f"""
                    SELECT name
                    FROM ingredients
                    WHERE sensitivity = '{sensitivity}'
                    """
            cursor.execute(query)
            ingredients = cursor.fetchall()
            return [ingredient["name"] for ingredient in ingredients]
    except Exception as e:
        print(e)


def get_pokemon_id(pokemon_name: str):
    try:
        with connection.cursor() as cursor:
            query = f"""
                    SELECT p_id
                    FROM pokemons
                    WHERE name = '{pokemon_name}'
                    """
            cursor.execute(query)
            result = cursor.fetchall()
            return result[0]["p_id"]
    except Exception as e:
        print(e)


def add_trainer_to_DB(name, town):
    try:
        with connection.cursor() as cursor:
            query = f"""
                    INSERT INTO trainers VALUES
                    (null, '{name}', '{town}')
                    """
            cursor.execute(query)
            connection.commit()
    except Exception as e:
        print(e)


def remove_pokemon_from_trainer(p_id, t_id):
    try:
        with connection.cursor() as cursor:
            query = f"""
                    DELETE FROM pokemons_trainers
                    WHERE p_id = '{p_id}' AND t_id = '{t_id}'
                    """
            cursor.execute(query)
            connection.commit()
    except Exception as e:
        print(e)


def update_pokemon_trainer(old_p_id, t_id, new_p_id):
    try:
        with connection.cursor() as cursor:
            query = f"""
                    UPDATE pokemons_trainers
                    SET p_id = '{new_p_id}'
                    WHERE t_id = '{t_id}' AND p_id = '{old_p_id}'
                    """
            cursor.execute(query)
            connection.commit()
    except Exception as e:
        print(e)
