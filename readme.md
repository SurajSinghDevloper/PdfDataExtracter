To run your Flask application using the dependencies listed in your requirements.txt file, you'll need to follow these steps:

1. Set Up a Virtual Environment (Optional but Recommended)
   A virtual environment helps you isolate your project’s dependencies from your system's Python installation, preventing conflicts with other projects.

On Unix or MacOS:
python3 -m venv venv
source venv/bin/activate
On Windows:
python -m venv venv
venv\Scripts\activate

2. Install the Dependencies
   Once your virtual environment is activated (you’ll see (venv) in your command prompt), install the dependencies from your requirements.txt file using pip:

bash
Copy code
pip install -r requirements.txt
This command will install all the libraries and packages listed in your requirements.txt.
and if you are on ubuntu run this command too:
sudo apt-get install libzbar0

3. Set Up Environment Variables
   If your Flask app uses environment variables (as indicated by the presence of python-dotenv in your requirements.txt), create a .env file in the root of your project with the necessary environment variables.

For example:

makefile
Copy code
FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=postgresql://user:password@localhost/dbname
SECRET_KEY=your-secret-key 4. Run the Flask App
You can run the Flask application in development mode using the following command:

flask run
If FLASK_APP is not set, specify the entry point of your app like so:

bash
Copy code
FLASK_APP=app.py flask run 5. Running the App with Gunicorn (for Production)
To run your Flask app with Gunicorn (typically used in production):

gunicorn -w 4 -b 0.0.0.0:8000 app:app

-w 4: Specifies 4 worker processes.
-b 0.0.0.0:8000: Binds the server to all interfaces on port 8000.
app:app: Indicates that app is the name of your Python file (without .py) and app is the name of the Flask app instance inside that file. 6. Running Tests
If you want to run tests with pytest, simply execute:

pytest
This will discover and run all the tests in your application.
