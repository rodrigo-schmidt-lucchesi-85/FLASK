# Part 4

---

In this part, We will introduce the database creation with SQLAlchemy and Flask-Migrate to handle the datababse migrations. **Flask-Migrate** is an extension that handles SQLAlchemy  database migrations for Flask applications using Alembic. The database  operations are made available through the Flask command-line interface  or through the Flask-Script extension. After you create the database using models.py use this command in your OS shell:

```bash
$ flask db init
```

This will add a migrations folder to your application. The contents of this folder need to be added to version control along with your other source files.

You can then generate an initial migration:

```bash
$ flask db migrate -m "Initial migration."
```

The migration script needs to be reviewed and edited, as Alembic  currently does not detect every change you make to your models. In  particular, Alembic is currently unable to detect table name changes,  column name changes, or anonymously named constraints. A detailed  summary of limitations can be found in the [Alembic autogenerate documentation](http://alembic.zzzcomputing.com/en/latest/autogenerate.html#what-does-autogenerate-detect-and-what-does-it-not-detect). Once finalized, the migration script also needs to be added to version control.

Then you can apply the migration to the database:

```bash
$ flask db upgrade
```

Then each time the database models change repeat the `migrate` and `upgrade` commands.

To sync the database in another system just refresh the migrations folder from source control and run the `upgrade` command.



Our Chapter 4 directory is organized as follows:

```bash
        . Chapter 4
        ├── app
        │   ├── forms.py
        │   ├── __init__.py
        │   ├── models.py
        │   ├── __pycache__
        │   │   ├── forms.cpython-38.pyc
        │   │   ├── __init__.cpython-38.pyc
        │   │   ├── models.cpython-38.pyc
        │   │   └── routes.cpython-38.pyc
        │   ├── routes.py
        │   └── templates
        │       ├── base.html
        │       ├── index.html
        │       └── login.html
        ├── app.db
        ├── config.py
        ├── main.py
        ├── migrations
        │   ├── alembic.ini
        │   ├── env.py
        │   ├── __pycache__
        │   │   └── env.cpython-38.pyc
        │   ├── README
        │   └── script.py.mako
        ├── Part_4.md
        └── __pycache__
            └── config.cpython-38.pyc
```

Our main application will be at the **app** folder, which will be the main repo with all necessary files to the **Flask** application. The **init.py** will be the initializer, with all needed modules to be working with Flask. The application configuration is managed from **config.py**. **Testing**, **development**, and **production** modes could be organized from this secure way to externally **config** the **Flask** application. The **routes.py** is guiding  the communication between front and back-end with the **endpoints** and **view functions**. The forms will be generated from **forms.py** with some required fields described in this document. The **templates** folder will handle the front-end **HTML** files. Finally, the **main.py** is the file to run Flask server (***flask run***).