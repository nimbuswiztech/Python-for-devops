import os

password = os.getenv("PASSWORD")
api_token = os.getenv("API_TOKEN")

print(f"Password: {password}")
print(f"API Token: {api_token}")