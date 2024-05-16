from flask import Flask, request, jsonify, render_template, url_for, send_file
import cruds.tab as t_crud
import cruds.word as w_crud
from database.database import init_db
from config import APP_DIR, SAVE_VOICE_DIR
import os

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.context_processor
def storage_processor():
    def storage_url(path):
        storage_dir = os.path.join(app.root_path, 'storage')
        return url_for('storage', filename=path, _external=True, _scheme='http')
    return dict(storage=storage_url)


@app.route('/storage/<path:filename>')
def storage(filename):
    return send_file(os.path.join(SAVE_VOICE_DIR, filename))


@app.route("/")
async def index():
    words = w_crud.get_all_words()
    tabs = t_crud.get_all_tabs()
    index = render_template('index.html', words=words, tabs=tabs)
    return index
    

@app.post('/word/add')
async def add_word():
    word = request.json.get('word')
    meaning = request.json.get('meaning')
    w = w_crud.create(word, meaning)
    words = w_crud.get_all_words()
    tabs = t_crud.get_all_tabs()
    index = render_template('index.html', words=words, tabs=tabs)
    return index


@app.post('/learn')
async def learn():
    print(request.form)
    word_ids = request.json
    words = []
    for id in word_ids:
        word = w_crud.read(id)
        if word:
            words.append(word)
    tabs = t_crud.get_all_tabs()
    return render_template('learn.html', words=words, tabs=tabs)


if __name__ == '__main__':
    app.run(
        host='localhost',
        port=8000
    )
