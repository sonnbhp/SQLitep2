import sqlite3
from car import Car
conn = sqlite3.connect("cars.db")

c =conn.cursor()
sql_create_table = """
    CREATE TABLE cars (
    name text,
    brand text,
    year integer
     )
"""
sql_insert = """
    INSERT INTO cars VALUES (:name, :brand, :year)
"""
def insert_car (car):
    with conn:
        c.execute(sql_insert,{"name":car.name,"brand":car.brand,"year":car.year})
        print("Car inserted !")

#c.execute(sql_create_table)

sql_select = """
    SELECT * FROM cars WHERE brand = :brand
"""

def select_car(brand):
    with conn:
        c.execute(sql_select ,{"brand":brand})
        return c.fetchall()

sql_update = """
    UPDATE cars set name = :name  WHERE brand = :brand
"""
def update_car (name,brand):
    with conn:
        c.execute(sql_select ,{"name":name, "brand":brand})
sql_delete = """
    DELETE FROM cars WHERE name = :name
"""
def delete_car (name):
    with conn:
        c.execute(sql_select,{"name":name})

    car1 = Car("C2150", "Mec", 1969)
    #insert_car(car1)

try:
    data = select_car("Mec")
    print(data)
except:
    print("Query error!!")
conn.close()