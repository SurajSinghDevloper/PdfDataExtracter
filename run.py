import os
from dotenv import load_dotenv
from app.app import create_app

# Load environment variables from the .env file
load_dotenv()

# Get the configuration name from environment variable, default to 'development'
config = os.getenv('FLASK_ENV', 'development')

# Create the Flask application instance
app = create_app(config)
# Set the maximum file size (30 GB = 30 * 1024 * 1024 * 1024 bytes)
app.config['MAX_CONTENT_LENGTH'] = 30 * 1024 * 1024 * 1024  # 30GB

if __name__ == "__main__":
    # Run the app with specified host and port
    app.run(host='172.16.16.207', port=8988, debug=(config == 'development'))
