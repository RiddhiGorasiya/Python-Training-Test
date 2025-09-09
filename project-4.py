import sqlite3

product_name = ['laptop', 'smartphone', 'headphone', 'keyboard', 'mouse']

formatted_products = list(map(str.capitalize, product_name))
conn = sqlite3.connect('products1.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS products1
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL)''')

for name in formatted_products:
    cursor.execute("INSERT INTO products1 (name) VALUES (?)", (name,))

conn.commit()

cursor.execute('SELECT id, name FROM products1')
rows = cursor.fetchall()

print("Products inserted successfully.")
for row in rows:
    print(f"{row[0]}. {row[1]}")
    
conn.close()