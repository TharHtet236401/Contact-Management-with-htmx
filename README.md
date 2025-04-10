# Contact-Management-with-htmx

# Django Project Setup


## Setting Up the Project

1. **Create a virtual environment:**
   It is recommended to create a virtual environment for your project to manage dependencies. Run the following command:
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4  **Migrate the database:**
   ```bash
   python manage.py migrate
   ```
5. **Create a superuser:** (optional)
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server:**
   Start the server with:
   ```bash
   python manage.py runserver
   ```
   You can now access your project at `http://127.0.0.1:8000/`.

## Additional Information
For more detailed instructions on using Django, refer to the [Django documentation](https://docs.djangoproject.com/en/stable/).
