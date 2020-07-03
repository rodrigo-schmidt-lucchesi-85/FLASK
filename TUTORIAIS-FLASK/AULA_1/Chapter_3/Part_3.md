# Part 3

---

In this part, We will start creating the login page to handle a remember me trigger. This login will be developed using by **flask_wtf**, a **Flask** library to create a **class-based** form, inherited from the related login template.

```bash
        . Chapter_3
        ├── app
        │   ├── forms.py
        │   ├── __init__.py
        │   ├── __pycache__
        │   │   ├── forms.cpython-38.pyc
        │   │   ├── __init__.cpython-38.pyc
        │   │   └── routes.cpython-38.pyc
        │   ├── routes.py
        │   └── templates
        │       ├── base.html
        │       ├── index.html
        │       └── login.html
        ├── config.py
        ├── main.py
        ├── Part_3.md
        └── __pycache__
            └── config.cpython-38.pyc
```

Our main application will be at the **app** folder, which will be the main repo with all necessary files to the **Flask** application. The **init.py** will be the initializer, with all needed modules to be working with Flask. The application configuration is managed from **config.py**. **Testing**, **development**, and **production** modes could be organized from this secure way to externally **config** the **Flask** application. The **routes.py** is guiding  the communication between front and back-end with the **endpoints** and **view functions**. The forms will be generated from **forms.py** with some required fields described in this document. The **templates** folder will handle the front-end **HTML** files. Finally, the **main.py** is the file to run Flask server (***flask run***).