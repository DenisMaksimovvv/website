# My Django Website

This is the repository for my Django website project. This website includes various pages such as a home page, an about page, a products page, and a store page.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.7 or higher.
- Django 3.1 or higher.

### Steps

1. Clone the repository to your local machine.
```bash
git clone https://github.com/<your_username>/my_django_website.git
```
2. Navigate into the project directory.
```bash
cd my_django_website
```
3. Install the required dependencies.
```bash
pip install -r requirements.txt
```
4. Run migrations.
```bash
python manage.py migrate
```

## Usage

You can run the development server to view the website.

```bash
python manage.py runserver
```

Once the server is running, you can navigate to `http://localhost:8000/` in your browser to view the website.

### URLs

- `/` - Home Page
- `/about` - About Page
- `/products` - Products Page
- `/store` - Store Page

