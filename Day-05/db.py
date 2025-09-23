import os

def connect_to_database():
    # Reading sensitive information from environment variables
    db_password = os.getenv('DB_PASSWORD')
    api_key = os.getenv('API_KEY1')
    
    if db_password and api_key:
        print("Connecting to database...")
        print(f"Using API Key: {api_key[:10]}...")  # Show only first 10 chars
        return True
    else:
        print("Missing required environment variables!")
        return False

# Usage
if connect_to_database():
    print("Connection successful!")
else:
    print("Connection failed!")