from flask import Flask
from database import init_db

app = Flask(__name__)

if __name__ == '__main__':
    init_db()
    # http://localhost:8000/
    app.run(
        host='localhost',
        port=8000
    )
