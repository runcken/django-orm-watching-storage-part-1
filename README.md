# Bank security console

This is internal repository for bank employees. If you got into this repository by accident, you will not be able to run it, because you dont have access to the database, but you will be able to freely use the code or see how the database queries are implemented.

Security console is a website that can be connected to a remote database with visits and passcards of our bank employees.

## How to install

Clone repository to your local device. To avoid problems with installing required additinal packages, use a virtual environment, for example:
```bash
runcken@dell:~/Documents/GitHub/django-orm-watching-storage-part-1$ python3 -m venv myenv
```

and then:

```bash
runcken@dell:~/Documents/GitHub/django-orm-watching-storage-part-1$ source myenv/bin/activate
```

Python3.12 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

The script uses additinal packages:

_django==5.2.*_

_psycopg2-binary==2.9.*_

_dotenv==0.9.9_

After all these manipulations you can run script using something like this:

```bash
(myenv)runcken@dell:~/Documents/GitHub/django-orm-watching-storage-part-1$ python3 main.py
```
As result you will see count of all employees passcards and separatly count of active passcards.

## Project Goals

The code is written for educational purposes on online-course for web-developers dvmn.org.
