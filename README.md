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


# create groups, customer, staff, manager

# enable SQLite ( macOS already includes the JSON1 extension by default)
- [doc](https://code.djangoproject.com/wiki/JSON1Extension)


# Run the server 
`python manage.py runserver`

### If `DEBUG = False` in eatery/settings.py
Make sure to run `python manage.py collectstatic`
- Although there is only one static image, this isn't ran it will not be displayed

### If `DEBUG = True` in eatery/settings.py
- 404 page won't be server, but instead a list of all routes are displayed