📖 Book & Movie Management Web App

A Flask-based web application to manage Books and Movies, including cover image upload, form-based CRUD operations, user authentication, and navigation features.

🚀 Features

📚 Book Management
View all books / non-hidden books
Add, edit, delete books
Detail view with metadata and cover

🎬 Movie Management
View all movies / non-hidden movies
Add, edit, delete movies
Detail view with metadata and cover

🖼️ Cover Images
Upload, display, and delete image files

👥 User Roles
Admin and user login via Flask-Login
Admin-only access to modification actions

🧭 Navigation & UX
Breadcrumb navigation between views
Responsive HTML templates (based on WTForms)

🔍 ISBN Scraping
Fetch metadata via ISBN input

🧪 Testing
Unit tests for core routes and forms
Separate test database (test.db)

🛠️ Setup Instructions

1. Clone the Repository
git clone https://github.com/JESchoett/py_booksite.git
cd py_booksite

2. Install Dependencies
pip install -r requirements.txt

3. Setup the Database

4. Run the Application
python run.py

5. Default Environment
Python 3.10+
SQLite database (no external DB setup needed)

📁 Folder Structure
booksite/
├── books/           # Book models, forms, templates
├── movies/          # Movie models, forms, templates
├── core/            # Index and routing logic
├── user_handeling/  # Login and signup
├── scripts/         # ISBN scraping, file operations
├── templates/       # Shared layout templates
├── app.py
├── run.py
├── tests/           # Unit tests