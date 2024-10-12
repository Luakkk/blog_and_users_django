Here’s your updated README file with credits added, formatted for GitHub:

---

# Simple Django Blog Project

This project is a simple blogging platform developed using Django. It allows users to create, edit, and delete blog posts, comment on posts, and follow other users. The platform also includes user authentication and profile management features.

## Features

- **User Registration and Authentication**
- **User Profile Management** (including profile picture uploads)
- **Blog Post Creation, Editing, and Deletion**
- **Commenting on Posts**
- **Follow/Unfollow Users**
- **Search Functionality** for Blog Posts
- **Pagination** for Blog Post Listing

## Requirements

- **Python 3.x**
- **Django** (latest stable version)
- **MongoDB** (with `djongo` for integration)
- **Virtual Environment** (recommended: `venv` or `virtualenv`)

## Installation

### 1. Clone the Repository

To get started, clone the repository from GitHub and navigate into the project directory:

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Create and Activate a Virtual Environment

Create and activate a virtual environment:

```bash
# On Windows
python -m venv myvenv
myvenv\Scripts\activate

# On macOS/Linux
python -m venv myvenv
source myvenv/bin/activate
```

### 3. Install Dependencies

Install all the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Configure MongoDB

Update `settings.py` with your MongoDB credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'your-database-name',
        'CLIENT': {
            'host': 'your-mongodb-host',
            'username': 'your-username',
            'password': 'your-password',
            'authSource': 'admin',
        }
    }
}
```

### 5. Apply Migrations

Prepare your database by applying migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser

Create a superuser account to access the Django admin:

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Access the application by visiting `http://127.0.0.1:8000/`.

## Usage

- **Admin Panel**: Go to `http://127.0.0.1:8000/admin/` and log in using the superuser account to manage users, posts, and more.
- **Create Blog Posts**: Use the blog interface to create, edit, and delete posts.
- **User Interactions**: Users can comment on posts, follow others, and update their profiles.

### Made by Alua Smanova

This Django project was built and maintained by **Alua Smanova**. If you have any questions or feedback, feel free to reach out or contribute via GitHub!

---
