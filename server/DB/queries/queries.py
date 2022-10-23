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
