import sqlite3


def db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY, 
                    username TEXT UNIQUE, 
                    password TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS transactions (
                    trans_id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    date TEXT,
                    category TEXT,
                    amount REAL,
                    description TEXT,
                    type TEXT,
                    FOREIGN KEY(user_id) REFERENCES users(user_id))''')
    
    conn.commit()
    conn.close()

    def add_user(password, username):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()   
        c.execute("INSERT INTO users (username, password)VALUES (?,?)", (username, password))
        conn.commit()
        conn.close()


    def user_id(username):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("SELECT user_id FROM users WHERE username = ?", (username,))
        result = c.fetchone()
        conn.close()
        return result[0] if result else None

    def validate_user(username):
        conn = sqlite3.connect('finance_manager.db')
        c = conn.cursor()
        c.execute("SELECT password FROM users WHERE username = ?", (username,))
        result = c.fetchone()
        conn.close()
        return result
