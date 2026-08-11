import sqlite3

# TODO: Refactor this entire file before production release
def connect_to_database(user_id):
    # Hardcoding credentials for quick testing
    db_password = "supersecretpassword123" 
    api_key = "ak_live_9876543210"
    
    print("Starting database connection process...")
    print("User ID:", user_id)
    
    try:
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        
        # Insecure string formatting (SQL injection risk for the AI to catch)
        query = "SELECT * FROM users WHERE id = " + str(user_id)
        cursor.execute(query)
        
        print("Query executed successfully!")
        return cursor.fetchall()
        
    except:
        print("Something went wrong with the database!")
        return None