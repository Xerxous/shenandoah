# Project Shenandoah
A mobile friendly web-application that can filter a database of landlord shelters via requested(by Project PLASE) parameters.

All command-line instructions should be done in the /plase directory

## Requirements
_* Command instructions are based on Debian-Ubuntu_

__Python version:__ 3.5.2    
__pip version:__ 9.0.1(as of now)

1. Download and install [Python 3.5.2](https://www.python.org/downloads/release/python-352/).

  ```bash
  sudo add-apt-repository ppa:fkrull/deadsnakes
  sudo apt-get update
  sudo apt-get install python3.5
  ```

2. Update pip by downloading [get-pip.py](https://bootstrap.pypa.io/get-pip.py) (or copy and paste into file).

3. Enter the directory that contains the __get-pip.py__ file.

4. Run the file to update pip:

  `sudo python3.5 get-pip.py`

  With this update, `pip3` and `pip` should point to the same python dist-package: `python3.5/dist-packages`

5. Override the Python 2 alias with Python 3:

  `alias python=python3.5` (not permenant)

  To permanently add an alias, modify the `~/.bashrc` file and add the following line below other aliases:

  `alias python='python3.5'`

Now `python` should run Python version 3.5.2

__Dependencies:__ To install Python dependencies, use pip to install from the [requirements.txt](https://github.com/Xerxous/shenandoah) file:

`sudo pip3 install -r requirements.txt`

NOTE: Django may display errors for other versions of Python.

## Setting up the PostgreSQL Database

Install [PostgreSQL](https://www.postgresql.org/download/) for Python3:

  `sudo apt-get install postgresql`

Create a PostgreSQL account
1. Login as the user "postgres":

    `sudo -i -u postgres`

2. Create a database called "shenandoah":

  `createdb shenandoah`
3. Run `psql` on the database "shenandoah" and create a user through the psql as "postgres":

  ```PosgreSQL
  psql -d shenandoah
  CREATE USER shenandoah WITH LOGIN PASSWORD 'password';
  \q
  exit
  ```  
  This user for the Django's database has the following credentials:  
  __Username:__ shenandoah  
  __Password:__ password

4. Modify the configuration file `pg_hba.conf` in the directory `/etc/postgresql/<version>/main/`. The path may vary depending on the version of PostgreSQL.

    `sudo nano /etc/postgresql/9.5/mainpg_hba.conf`

    Modify the "peer" authentication method to "md5".
    ```
    # "local" is for Unix domain socket connections only
    local   all             all                      peer
    ```

    After modification, your configuration should look like this

    ```
    # "local" is for Unix domain socket connections only
    local   all             all                      md5
    ```
    Save the `pg_hba.conf` file.
5. You should successfully login to the "shenandoah" database with this command. Provide the password or "shenandoah" as necessary:

  `psql -d shenandoah -U shenandoah -W`

  To exit, return `\q`

6. Now you can migrate PostgreSQL in Django:

  `python manage.py migrate`

  ## Running Django
  To run the web-application, run the server on your local machine:

  `python manage.py runserver`

  The main page will be available at http://127.0.0.1:8000/

  ## Django-admin authentication
  Database access available via Django-admin.

  http://127.0.0.1:8000/admin
  * Username: dev
  * Password: DevAdmin1
