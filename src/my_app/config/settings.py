import os

from dotenv import load_dotenv

# Load environment variables from a .env file at the project root
load_dotenv()

# --- Application Settings ---
# It's good practice to provide a default value for non-secret settings
APP_NAME = os.getenv("APP_NAME", "MyApp")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

# --- Example for Secrets ---
# For secrets, it's better to fail if they are not set.
# API_KEY = os.getenv("API_KEY")
# if not API_KEY:
#     raise ValueError("A secret API_KEY must be set in the .env file.")
