import pymysql


def insert_ingredients(connection, ingredients, sensetivity):
    try:
        with connection.cursor() as cursor:
            query = f"""
                    INSERT INTO ingredients VALUES
                    {",".join([
                        f'(null, "{ingredient}", "{sensetivity}")' 
                        for ingredient in ingredients
                        ])
                    }
                    """
            cursor.execute(query)
            connection.commit()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    dairy_ingredients = [
        "Cream",
        "Cheese",
        "Milk",
        "Butter",
        "Creme",
        "Ricotta",
        "Mozzarella",
        "Custard",
        "Cream Cheese",
    ]
    gluten_ingredients = ["Flour", "Bread", "spaghetti", "Biscuits", "Beer"]

    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="recipes_app",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor,
    )
    insert_ingredients(connection, dairy_ingredients, "dairy")
    insert_ingredients(connection, gluten_ingredients, "gluten")
