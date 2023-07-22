Requirements:

asgiref==3.3.1
autopep8==1.5.4
coverage==5.3.1
Django==3.1.4
flake8-django==1.1.1
isort==5.7.0
mccabe==0.6.1
Pillow==8.0.1
pycodestyle==2.6.0
pyflakes==2.2.0
pytz==2020.4
sqlparse==0.4.1
testfixtures==6.17.1
toml==0.10.2

pip install Django-countries

Instructions:

Customer View
1. After installing all dependencies, run the server using 
    python manage.py runserver
2. Register an account using the registration page.
3. Log into the account registered using the login button in the header.
4. Browse the website. Feel free to check all product pages, category pages, about us section, and the like.
5. Add a product to the cart. The cart quantity should automatically update with the total quantity of products updated.
6. Test out cart modification features. Edit the quantity of products or delete them entirely. The total should update accordingly.
7. Click the proceed to quotation button. Enter details accordingly and check the cart breakdown to ensure it is correct.
8. Submit a quotation. You should automatically be redirected to a submission page.
9. Logout using the logout button in the header.

Admin View
1. After installing all dependencies, run the server using python manage.py runserver
2. Using terminal, create a superuser account using the following command:
    python manage.py createsuperuser and enter details accordingly
3. From the server, add "/admin" in the browser url.
4. Log in using the superuser account you just created.
5. View all existing users, products, and categories. Modify them accordingly or delete them entirely.
6. You may also test the database by creating new users in the front-end page and checking the database in the admin view.