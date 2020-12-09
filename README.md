### This provide the instruction to get the app running on your machine

# Requirement: 
- Python 3.9.0
- virtualenv [doc](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

# Pip install a virtualenv
**On macOS and Linux:**

`python3 -m pip install --user virtualenv`

**On Windows:**

`py -m pip install --user virtualenv`


# Create a virtual env, and activate it
- virtualenv [doc](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
# Switch to the director where manage.py is located
# Install the required python packages by: 
`pip install -r requirements.txt`


# enable SQLite ( macOS already includes the JSON1 extension by default)
- [doc](https://code.djangoproject.com/wiki/JSON1Extension)


# Run the server 
`python manage.py runserver`

### If `DEBUG = False` in eatery/settings.py
Make sure to run `python manage.py collectstatic`
- Although there is only one static image, this isn't ran it will not be displayed

### If `DEBUG = True` in eatery/settings.py
- 404 page won't be server, but instead a list of all routes are displayed

### Name: 
# **the Neighborhood Eatery -by WebX **

## Team Member and Roles: 
#### Winton Wong: 
- Backend, deployment

#### Julio Gonzalez Gonzalez: 
- Frontend interactive, UI design, html/css, database designs and implementations

## Deployable Website
> **Website:** http://eateryx.wintonw.com

> **Github:** https://github.com/cse264/final-project-webx/tree/live

> **Test Accounts: {user, email, password}:** 
> - {customer, user@test.com, useruseruser}, 
> - {staff, staff@test.com, staffstaff}, 
> - {manager, manager@test.com, managermanager}

> **PayPal:**
> - sb-nhogx1433147@personal.example.com
> - rrY_%?g9

### User Story/Use Case
> **Customers** views the menu online, order and pay for pickup, and checks order status and detail when logged in. 

> **Manager** can see, accept/reject, change status, cancel, and edit the order of customers and menu items.

> **Manager/restaurant associates** can see, accept/reject, and change order status of the order of customers

### Functionality
- A open source website platform for restaurants to accept and manage orders for pickup, tools to analyze sales, and managing account users
- Customers can create accounts managed by cookies to place, pay, and view orders
- Analyze sales and use Google Analytics in order to show website performance with customer base
- Sales are made through a PayPal api(sandbox), payer ID is then recorded and added into the database



### Technical Design
- Customers' cart are managed by cookies
- Customer log in is managed by sessions
- Restaurant accounts (manager, restaurant staff) can be reassigned by the superuser or manager
- Customer can track their order status (order accepted, order preparing, order ready, canceled), logged in (full detail) and logged out (partial detail)
- Manager accounts can change and edit each order and have access to the admin page where users and database is controlled
- Restaurant Staff accounts have access to the dashboard where they can can change order status (order accepted, order preparing, order ready) and update on the customers account
- PayPal, ID of payer is recorded into database and posts the order to the dashboard

### Tools/Libraries/Frameworks/Languages
- Backend: Django, Python, JavaScript
- Frontend: Bootstrap, JQuery, HTML/CSS/JS
- Database: SQLite
- Payment: PayPal
- Whitenoise: A middleware that help serve static files in deployment