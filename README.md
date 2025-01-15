# Candidate App Project

This is the `candidate_app`, a Django-based project for managing candidates, user authentication, and voting functionality.

## **Setup Instructions**

### Clone the Repository
- Clone the repository to your local machine:
  ```bash
  git clone https://github.com/Thabo353/L3T10---Capstone-Project---Consolidation
  ```

### Navigate to the Project Directory
- Move into the project directory:
  ```bash
  cd candidate_app
  ```

### Create a Virtual Environment
On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
- Install the required dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### Apply Migrations
- Run the following commands to apply database migrations:
  ```bash
  python manage.py makemigrations candidate_app
  python manage.py migrate
  ```

### Start the Server
- Run the development server:
  ```bash
  python manage.py runserver
  ```

### Create a Superuser
- Create a superuser account for accessing the admin interface:
  ```bash
  python manage.py createsuperuser
  ```

### Test Locally
- Access the application in your browser at:
  [http://localhost:8000](http://localhost:8000)

### Register Candidates and Amend Policies
- Use the admin interface or application features to register candidates and update policies.

### Build the Docker Image
- Build the Docker image for the project:
  ```bash
  docker build -t thabokganyago353/candidate_app .
  ```

### Run the Docker Container
- Start the application using Docker:
  ```bash
  docker run -p 8000:8000 thabokganyago353/candidate_app:latest
  ```

## **Features**
- User registration and login/logout functionality.
- Display a list of candidates.
- Authenticated users can vote for candidates.
- Policies view (to be implemented).
- Learn more (to be implemented).

## **Requirements**
- Docker installed on your system.
- Python version 3.10 (if running locally).
- Django framework installed.
