import sqlite3

# Function to connect to the database
def connect_db():
    return sqlite3.connect("snippets.db")

# Function to insert a snippet
def insert_snippet(title, language, code, tags):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO snippets (title, language, code, tags) VALUES (?, ?, ?, ?)",
                   (title, language, code, tags))
    conn.commit()
    conn.close()
    print("✅ Snippet added successfully!")

# Function to fetch all snippets
def get_all_snippets():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM snippets")
    data = cursor.fetchall()
    conn.close()
    return data

# Function to search snippets by language or tag
def search_snippets(search_text):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM snippets WHERE language LIKE ? OR tags LIKE ?", 
                   ('%' + search_text + '%', '%' + search_text + '%'))
    data = cursor.fetchall()
    conn.close()
    return data

# === TESTING === #
if __name__ == "__main__":
    # Insert some test snippets
    insert_snippet("Bubble Sort", "Python", "def bubble_sort(): pass", "sorting, algorithm")
    insert_snippet("Quick Sort", "Python", "def quick_sort(): pass", "sorting, algorithm")
    insert_snippet("SQL Select", "SQL", "SELECT * FROM table_name;", "query, database")

    # Fetch & print all snippets
    snippets = get_all_snippets()
    print("📌 All Snippets:")
    for s in snippets:
        print(s)

    # Search snippets
    search_result = search_snippets("Python")
    print("\n🔍 Search Result (Python Snippets):")
    for s in search_result:
        print(s)

import sqlite3

conn = sqlite3.connect("snippets.db")  # Change name if your database file is different
cursor = conn.cursor()

cursor.execute("SELECT * FROM snippets")
snippets = cursor.fetchall()

for snippet in snippets:
    print(snippet)

conn.close()

