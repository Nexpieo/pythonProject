import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)

    return connection


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_products(conn, product):
    try:
        sql = '''INSERT INTO products 
        (product_title, price, quantity) 
        VALUES (?, ?, ?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_quantity(conn, product):
    try:
        sql = '''UPDATE products SET quantity = ?
        WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_price(conn, product):
    try:
        sql = '''UPDATE products SET price = ?
        WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_product(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products_by_name(conn, name):
    try:
        name = f"%{name}%"
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (name,))
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)



def select_products_by_price_quantity(conn):
    try:
        sql = '''SELECT * FROM products WHERE price < 100 AND quantity > 5'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)



sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL, 
price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER(3) NOT NULL DEFAULT 0
)
'''

connection = create_connection('hw.db')
select_all_products(connection)
update_price(connection, (100, 2))
update_quantity(connection, (40, 12))
delete_product(connection, 15)
select_products_by_price_quantity(connection)
select_products_by_name(connection, "чипсы")
if connection is not None:
    print('Connected successfully')
    create_table(connection, sql_create_products_table)
    insert_products(connection, ('сок Pepsi', 90, 30))
    insert_products(connection, ('сок Cola', 90, 35))
    insert_products(connection, ('сок Садочок', 130, 20))
    insert_products(connection, ('семечки Джинн тыквенные', 125, 15))
    insert_products(connection, ('семечки Джинн соленные', 125, 15))
    insert_products(connection, ('семечки Джинн обычные', 115, 15))
    insert_products(connection, ('шоколад Alpen Gold', 80, 30))
    insert_products(connection, ('шоколад Ozera', 70, 20))
    insert_products(connection, ('шоколад Snickers', 35, 40))
    insert_products(connection, ('шоколад Albeni', 35, 35))
    insert_products(connection, ('шоколад MilkyWay', 25, 35))
    insert_products(connection, ('шоколад Bounty', 35, 45))
    insert_products(connection, ('чипсы Пир', 100, 30))
    insert_products(connection, ('чипсы Lays', 120, 20))
    insert_products(connection, ('чипсы Grizzly', 100, 20))