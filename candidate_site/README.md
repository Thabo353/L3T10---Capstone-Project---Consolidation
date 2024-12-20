# Candidate App Project

This is the `candidate_app`, a Django-based project for managing candidates, user authentication, and voting functionality.

## **Setup Instructions**

- Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Thabo353/L3T10---Capstone-Project---Consolidation  
- Navigate to the project directory:
   cd candidate_app

- Create visual environment
   ```bash
On Windows:
   python -m venv venv
   venv\Scripts\activate

On macOS/Linux: 
   python3 -m venv venv
   source venv/bin/activate

- Install Dependencies:
   pip install -r requirements.txt                  

- 1st run python manage.py makemigrations into candidate_app and run python manage.py migrate.

- Start the server: 
   python manage.py runserver

- Create superuser and password.

- Do a local run and login.
   http://localhost:8000

- Register your candidates and also amend policies.

- Strat building the image:
   docker build -t thabokganyago353/candidate_app .

- Run docker:
   docker run -p 8000:8000 thabokganyago353/candidate_app:latest


## **Features** 
- User registration and login/logout functionality.
- Display a list of candidates.
- Authenticated users can vote for candidates.
- Policies view (to be implemented). 
- Lear more (to be implemented)

### **Requirements** 
- Docker installed on your system.
- Python version 3.10 (if running locally).
- Django framework installed.