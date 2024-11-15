""" create app for user air """
import sqlite3

db = sqlite3.connect("app.db") # connected file database
cr = db.cursor()
cr.execute("CREATE TABLE IF NOT EXISTS user5 (name TEXT, phone TEXT, price INTEGER, from_country TEXT, to_country TEXT)")

# massage input
MASSAGE = """
1 - Add user
2 - Search user
3 - Delete user
4 - Update user
5 - Quite app
Choose : 
"""

# insert ------------------------------------------------------------------------------------

def insert_data():
    """ insert data to database """

    name = input("name: ").strip().lower()
    phone = input("phone: ").strip()
    price = int(input("price: ").strip())
    from_country = input("from: ").strip().lower()
    to_country = input("to: ").strip().lower()
    cr.execute(f"INSERT INTO user5 (name,phone,price,from_country,to_country) VALUES ('{name}', '{phone}', {price}, '{from_country}', '{to_country}')")

# search -----------------------------------------------------------------------------------

def search_data():
    """ search to database """
    name = input("enter name : ").strip().lower()
    cr.execute(f"SELECT * FROM user5 WHERE name = '{name}'")
    z = cr.fetchall()
    print(z)

# delete ------------------------------------------------------------------------------------

def delete_data():
    """ delete data """
    name = input("enter name to delete: ").strip().lower()
    cr.execute(f"DELETE FROM user5 WHERE name = '{name}'")

# update ------------------------------------------------------------------------------------

def update_user():
    """ update user data"""

    old_name = input("enter old name: ")  # choose old name you wanted update
    cr.execute(f"SELECT * FROM user5 WHERE name = '{old_name}'")

# create new data for your old name

    name = input("name: ").strip().lower()
    phone = input("phone: ").strip()
    price = int(input("price: ").strip())
    from_country = input("from: ").strip().lower()
    to_country = input("to: ").strip().lower()
    cr.execute(f"UPDATE user5 SET name = '{name}',phone = '{phone}',price = {price},from_country = '{from_country}',to_country = '{to_country}' WHERE name = '{old_name}'")

# if condition from choose input -------------------------------------------------------------------------------------------------------------------

while True:

    choose_input = input(MASSAGE)

    if choose_input == '1':
        insert_data()
        db.commit()

    elif choose_input == '2':
        search_data()
        db.commit()

    elif choose_input == '3':
        delete_data()
        db.commit()

    elif choose_input == '4':
        update_user()
        db.commit()

    elif choose_input == '5':
        db.commit()
        db.close()
        break

    else:
        print("please choose (1,2,3,4,5)")


