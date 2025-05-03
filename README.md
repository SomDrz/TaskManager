Project Setup

Step 1: Clone the Repository

git clone https://github.com/SomDrz/task-manager.git


cd django-tasks-assignment

Step 2: Create Virtual Environment & Install Requirements



python -m venv venv

For Windows: venv\Scripts\activate

pip install -r requirements.txt

If you don’t have requirements.txt, create one:



Django>=4.2
djangorestframework
psycopg2-binary  # Only if you're using PostgreSQL
python-dotenv


2. Configure Environment

Step 1: Create a .env file 

env

DB_NAME=yourdbname

DB_USER=yourdbuser

DB_PASSWORD=yourdbpassword

DB_HOST=localhost

DB_PORT=5432


Step 2: Update settings.py


Make sure your settings.py reads from .env using:


from dotenv import load_dotenv
load_dotenv()


3. Apply Migrations & Create Superuser

python manage.py makemigrations

python manage.py migrate

4. Run the Server
   
python manage.py runserver

API is now available at: http://localhost:8000/api/tasks/

 5. Run Unit Tests

python manage.py test
