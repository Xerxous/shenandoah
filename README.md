# Project Shenandoah
A mobile friendly web-application that can filter a database of landlord shelters via requested(by Project PLASE) parameters.

All command-line instructions should be done in the /plase directory

## Requirements
_* Command instructions are based on Debian-Ubuntu_

__Python version:__ 3.5.2    
__pip version:__ 9.0.1(as of now)

1. Download and install [Python 3.5.2](https://www.python.org/downloads/release/python-352/).

  `sudo apt-get install python3.5`

2. Update pip by downloading [get-pip.py](https://bootstrap.pypa.io/get-pip.py) (or copy and paste into file).

3. Enter the directory that contains the __get-pip.py__ file.

4. Run the file to update pip:

  `sudo python3 get-pip.py`

5. Override the Python 2 alias with Python 3:

  `alias python=python3` (not permenant)

  To permanently add an alias, modify the `~/.bashrc` file and add the following line below other aliases:

  `alias python='python3'`

Now `python` should run Python version 3.5.2

__Dependencies:__ To install Python dependencies, use pip to install from the requirements file:

`pip install -r requirements.txt`

NOTE: Django may display errors for other versions of Python.

## Running Django
To run the web-application, run the server on your local machine:

`python manage.py runserver`

The main page will be available at http://127.0.0.1:8000/

## Django-admin authentication
Database access available via Django-admin.

http://127.0.0.1:8000/admin
* Username: dev
* Password: DevAdmin1

## Setting up the PostgreSQL Database

Install [PostgreSQL](https://www.postgresql.org/download/) for Python3:

  `sudo apt-get install postgresql`

Create a PostgreSQL account
1. Login as the user "postgres":

    `sudo -i -u postgres`

2. Create a database called "plase":

  `createdb plase`
3. Create a user with the credentials below:

  `createuser plase -W`  

  __Username:__ plase  
  __Password:__ password

4. You should successfully login to the "plase" database with this command:

  `psql -d plase -U plase -W`

  To exit, return `\q`

5. Now you should be able to migrate in Django:

  `python manage.py migrate`
