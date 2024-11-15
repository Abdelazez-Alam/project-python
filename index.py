""" create app for user air """
# 1- create input data from user
# 2- create file database
# 3- merge data with database
# 4- loop data user
# 5- quite app
import sqlite3

db = sqlite3.connect("app.db")
cr = db.cursor()
cr.execute("CREATE TABLE IF NOT EXISTS user5 (name TEXT, phone TEXT, price INTEGER, from_country TEXT, to_country TEXT)")

MASSAGE = """
1 - Add user
2 - Search user
3 - Delete user
4 - Update user
5 - Quite app
Choose : 
"""
choose_input = input(MASSAGE)



def insert_data():
    """ insert data to database """
    name = input("name: ").strip().lower()
    phone = input("phone: ").strip()
    price = int(input("price: ").strip())
    from_country = input("from: ").strip().lower()
    to_country = input("to: ").strip().lower()
    cr.execute(f"INSERT INTO user5 (name,phone,price,from_country,to_country) VALUES ('{name}', '{phone}', {price}, '{from_country}', '{to_country}')")

def search_data():
    """ search to database """
    name = input("enter name : ").strip().lower()
    cr.execute(f"SELECT * FROM user5 WHERE name = '{name}'")
    z = cr.fetchall()
    print(z)
def delete_data():
    """ delete data """
    name = input("enter name to delete: ").strip().lower()
    cr.execute(f"DELETE FROM user5 WHERE name = '{name}'")
def update_user():
    """ update user data"""
    old_name = input("enter old name: ")
    cr.execute(f"SELECT * FROM user5 WHERE name = '{old_name}'")

    name = input("name: ").strip().lower()
    phone = input("phone: ").strip()
    price = int(input("price: ").strip())
    from_country = input("from: ").strip().lower()
    to_country = input("to: ").strip().lower()
    cr.execute(f"UPDATE user5 SET name = '{name}',phone = '{phone}',price = {price},from_country = '{from_country}',to_country = '{to_country}' WHERE name = '{old_name}'")

if choose_input == '1':
#create input
    insert_data()
elif choose_input == '2':
    search_data()
elif choose_input == '3':
    delete_data()
elif choose_input == '4':
    update_user()
elif choose_input == '5':
    pass

db.commit()
db.close()
