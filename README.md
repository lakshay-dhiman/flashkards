# Local Setup
- Clone the project
- Run `pip install -r requirements.txt` to install all dependencies

# Local Development Run
- `python main.py` It will start the flask app in `development`. Suited for local development.

# Replit run
- Go to shell and run
    `pip install --upgrade poetry`
- Click on `main.py` and click button run
- The web app will be availabe at https://ForestgreenSereneEllipses.lakshay1208.repl.co
- Format https://<replname>.<username>.repl.co

# Folder Structure
- `database.db` is the sqlite DB. It can be anywhere on the machine. Adjust the path in `main.py`. This app ships with one required for testing.
- `/` is where our application code is
- `static` - default `static` files folder. It serves at '/static' path.
- `templates` - Default flask templates folder

/
├── __pycache__/
│   ├── api.cpython-39.pyc
│   ├── main.cpython-39.pyc
│   └── models.cpython-39.pyc
├── app/
│   ├── __init__.py
│   ├── __pycache__/
│   │   ├── __init__.cpython-39.pyc
│   │   ├── api.cpython-39.pyc
│   │   ├── controler.cpython-39.pyc
│   │   ├── database.cpython-39.pyc
│   │   ├── databse.cpython-39.pyc
│   │   └── models.cpython-39.pyc
│   ├── api.py
│   ├── controler.py
│   ├── database.py
│   └── models.py
├── db.sqlite3
├── main.py
├── static/
│   ├── assets/
│   │   ├── add.svg
│   │   ├── add_deck.svg
│   │   └── prev.svg
│   ├── js/
│   │   ├── cards.js
│   │   └── decks_add.js
│   └── style/
│       ├── cards.css
│   └── register.html
└── tree.py
