"""SQLite3 database management for game top-ups"""
import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), 'instance', 'topup.db')

def get_db_connection():
    """Create and return a database connection"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with tables"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create games table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            category TEXT NOT NULL
        )
    ''')
    
    # Create topup_transactions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS topup_transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            game_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            currency TEXT DEFAULT 'USD',
            status TEXT DEFAULT 'pending',
            transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (game_id) REFERENCES games(id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

def add_user(username, email, phone=None):
    """Add a new user"""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO users (username, email, phone)
            VALUES (?, ?, ?)
        ''', (username, email, phone))
        conn.commit()
        return {'success': True, 'user_id': cursor.lastrowid}
    except sqlite3.IntegrityError as e:
        return {'success': False, 'error': str(e)}
    finally:
        conn.close()

def add_game(name, category):
    """Add a new game"""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO games (name, category)
            VALUES (?, ?)
        ''', (name, category))
        conn.commit()
        return {'success': True, 'game_id': cursor.lastrowid}
    except sqlite3.IntegrityError as e:
        return {'success': False, 'error': str(e)}
    finally:
        conn.close()

def record_topup_transaction(user_id, game_id, amount, currency='USD'):
    """Record a top-up transaction"""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO topup_transactions (user_id, game_id, amount, currency, status)
            VALUES (?, ?, ?, ?, 'completed')
        ''', (user_id, game_id, amount, currency))
        conn.commit()
        return {'success': True, 'transaction_id': cursor.lastrowid}
    except sqlite3.IntegrityError as e:
        return {'success': False, 'error': str(e)}
    finally:
        conn.close()

def get_user_transactions(user_id):
    """Get all transactions for a user"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT t.*, g.name as game_name
        FROM topup_transactions t
        JOIN games g ON t.game_id = g.id
        WHERE t.user_id = ?
        ORDER BY t.transaction_date DESC
    ''', (user_id,))
    transactions = cursor.fetchall()
    conn.close()
    return [dict(row) for row in transactions]

def get_all_transactions():
    """Get all transactions"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT t.*, u.username, g.name as game_name
        FROM topup_transactions t
        JOIN users u ON t.user_id = u.id
        JOIN games g ON t.game_id = g.id
        ORDER BY t.transaction_date DESC
    ''')
    transactions = cursor.fetchall()
    conn.close()
    return [dict(row) for row in transactions]

def update_transaction_status(transaction_id, status):
    """Update transaction status"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE topup_transactions
        SET status = ?
        WHERE id = ?
    ''', (status, transaction_id))
    conn.commit()
    conn.close()
    return {'success': True}
