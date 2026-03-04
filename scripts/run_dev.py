
import os
import sys

# Add the 'src' directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
src_path = os.path.join(project_root, 'src')
sys.path.insert(0, src_path)

from my_app.main import main

if __name__ == "__main__":
    print(f"Starting my_app from {src_path}...")
    main()