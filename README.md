# This is a demo project -> for practicing models and relationships along with some admin page customization

## To install and use this project follow the steps below:

1. Clone the repo, or download the files
    - to clone ``` git clone --branch models-and-relationships --single-branch https://github.com/prakashtaz0091/classes.git models-relationships ```
    - to download [click-here](https://github.com/prakashtaz0091/classes/archive/refs/heads/models-and-relationships.zip)
---
2. Create and activate virtual environment according to your OS
    - Windows
      ```
      python -m venv virtual_env
      virtual_env\Scripts\activate
      ```
   - Linux/MacOS
     ```
     pip install virtualenv
     virtualenv env
     source env/bin/activate
     ```
---
3. Install required dependencies
   ```
   pip install -r requirements.txt
   ```
---
4. Apply migrations
   ```
   python manage.py migrate
   ```
---
5. Create a superuser (Optional)
   ```
   python manage.py createsuperuser
   ```
   follow the instructions
---
6. Run development server
   ```
   python manage.py runserver
   ```
---
7. Ctrl + Click on the hosted link, or in browser type ```http://localhost:8000``` and hit enter
