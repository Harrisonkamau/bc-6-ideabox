
import os.path
import sqlite3

with sqlite3.connect('posts.db') as connection:
    c = connection.cursor()
    # c.execute("""DROP TABLE posts""")
    c.execute("CREATE TABLE posts(title TEXT, description TEXT)")
    c.execute('INSERT INTO posts VALUES("Andela Fellowship", "Becoming an Andela Fellow is all i dream about")')
    c.execute('INSERT INTO posts VALUES("Bootcamp", "I hope to successfully win the race")')
    
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "Posts.db")
    # c.commit()
