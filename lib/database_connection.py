import sqlite3

# Create the database connection and cursor
CONN = sqlite3.connect('reviews.db')
CURSOR = CONN.cursor()
