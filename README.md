# Contact-Management-with-htmx

# Django Project Setup

## Prerequisites
Before you begin, ensure you have met the following requirements:
- You have Python 3.x installed on your machine.
- You have pip installed for managing Python packages.
- You have Django installed. You can install it using pip:
  ```bash
  pip install django
  ```

## Setting Up the Project

1. **Create a new Django project:**
   Open your terminal and run the following command:
   ```bash
   django-admin startproject contacthub
   ```

2. **Navigate into the project directory:**
   ```bash
   cd contacthub
   ```

3. **Create a new Django app:**
   To create a new app called `contacts`, run:
   ```bash
   python manage.py startapp contacts
   ```

4. **Add the app to your project:**
   Open `contacthub/settings.py` and add `'contacts',` to the `INSTALLED_APPS` list.

5. **Set up the database:**
   By default, Django uses SQLite. You can run the following command to create the database:
   ```bash
   python manage.py migrate
   ```

6. **Run the development server:**
   Start the server with:
   ```bash
   python manage.py runserver
   ```
   You can now access your project at `http://127.0.0.1:8000/`.

## Additional Information
For more detailed instructions on using Django, refer to the [Django documentation](https://docs.djangoproject.com/en/stable/).

