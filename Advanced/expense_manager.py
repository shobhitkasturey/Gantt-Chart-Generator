import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from database import get_user_id

def log_transaction(username, date, category, amount, description, trans_type):
    user_id = get_user_id(username)
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO transactions (user_id, date, category, amount, description, type) VALUES (?, ?, ?, ?, ?, ?)",
              (user_id, date, category, amount, description, trans_type))
    conn.commit()
    conn.close()

def view_transactions(username):
    user_id = get_user_id(username)
    conn = sqlite3.connect('data.db')
    df = pd.read_sql_query("SELECT * FROM transactions WHERE user_id = ?", conn, params=(user_id,))
    conn.close()
    return df

def visualize_transactions(username):
    df = view_transactions(username)
    if df.empty:
        print("No transactions to visualize.")
        return
    
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    
  
    expense_df = df[df['type'] == 'expense']
    category_totals = expense_df.groupby('category')['amount'].sum()
    category_totals.plot(kind='bar', title='Expenses by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Amount')
    plt.tight_layout()
    plt.savefig('expenses_by_category.png')
    plt.show()
    
    
    daily_totals = expense_df.resample('D')['amount'].sum()
    daily_totals.plot(kind='line', title='Daily Expenses Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Amount')
    plt.tight_layout()
    plt.savefig('daily_expenses_over_time.png')
    plt.show()