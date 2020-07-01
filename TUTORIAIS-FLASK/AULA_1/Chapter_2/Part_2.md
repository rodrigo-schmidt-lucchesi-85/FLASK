# Part 2

---

In this part, we're going to create a new structure to the **view functions**, using the **Jinja2** engine to handle the **route** communication with the **HTML** files, located at the templates folder. It will be structured as the following tree:

```bash
    .
    ├── Part_2
    │   ├── app
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── __init__.cpython-38.pyc
    │   │   │   └── routes.cpython-38.pyc
    │   │   ├── routes.py
    │   │   └── templates
    │   │       ├── base.html
    │   │       └── index.html
        └── main.py
```

Our main application will be at the **app** folder, which will be the main repo with all necessary files to the **Flask** application. The **init.py** will be the initializer, with all needed modules to be working with Flask. The **routes.py** is guiding  the communication between front and back-end with the **endpoints** and **view functions**. The **templates** folder will handle the front-end **HTML** files. Finally, the **main.py** is the file to run Flask server (***flask run***).