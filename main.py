from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    # http://localhost:8000/
    app.run(
        host='localhost',
        port=8000
    )
