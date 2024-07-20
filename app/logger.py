import sqlite3

def init_db(db_path='activity_log.db'):
    conn = sqlite3.connect(db_path)
    
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS activity_log (
                id INTEGER PRIMARY KEY,
                start_time REAL,
                end_time REAL,
                total_time REAL,
                app TEXT,
                context TEXT
            )
        ''')
        conn.commit()
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def log_to_db(start_time, end_time, app, context, db_path='activity_log.db'):
    conn = sqlite3.connect(db_path)
    
    if app is None:
        print("No application detected.")
        return
    total_time = end_time - start_time
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO activity_log (start_time, end_time, total_time, app, context)
            VALUES (?, ?, ?, ?, ?)
        ''', (start_time, end_time, total_time, app, context))
        conn.commit()
        print(f"Logged to DB: start_time={start_time}, end_time={end_time}, total_time={total_time}, app={app}, context={context}")
    except Exception as e:
        print(f"Error logging to database: {e}")
    finally:
        conn.close()