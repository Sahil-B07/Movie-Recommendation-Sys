# Movie Recommendation System

## Description

This project implements a movie recommendation system using collaborative filtering. It tracks user interactions with movie cards, updating their watch history in a PostgreSQL database. Based on this watch history, the system generates recommendations for the user.

**_NOTE:_** For now the click functionality is under development so instead inorder to get things done just update the **watched** field in the database manually (using django admin).

## Installation

### Prerequisites

- Python 3.x
- Django
- PostgreSQL

### Steps

1. Clone the repository:

   ```bash
   https://github.com/Sahil-B07/Movie-Recommendation-Sys.git
   ```

2. Install Requirements

    ```bash
    pip install -r requirements.txt
    ```

3. Install Django & Postgres 

    ```bash
    python -m pip install Django
    ```
    
    ```bash
    python -m pip install Django
    ```

4. Create .env file in the project directory and add the database details

    ```bash
    PG_NAME = 'DB_NAME'
    PG_USER = 'USER_NAME'
    PG_HOST = 'localhost'
    PG_PASSWORD = 'USER_PASSWORD'
    ```

    If not, create a user with database in postgresql.

5. Create a super user & migrations

    ```bash
    python manage.py createsuperuser
    ```

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Login to the django-admin and create a profile in Person Model. Add some movie names in the watched field http://127.0.0.1:8000/admin

![Add Watched](/web/static/web/img1.jpg)

7. Now transfer the csv data into postgres db

    ```bash
    python manage.py import_movies tmdb_5000_movies.csv
    ```
8. Run the server

    ```bash
    python manage.py runserver
    ```

    Test: http://127.0.0.1:8000/web/
