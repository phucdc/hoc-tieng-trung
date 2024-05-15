from flask import Flask, request, jsonify, render_template
import cruds.tab as t_crud
import cruds.word as w_crud
from database.database import init_db

app = Flask(__name__, template_folder='templates', static_folder='voices')


@app.route("/")
async def index():
    words = w_crud.get_all_words()
    tabs = t_crud.get_all_tabs()
    return render_template('index.html', words=words, tabs=tabs)


@app.post('/word/add')
async def add_word():
    word = request.json.get('word')
    meaning = request.json.get('meaning')
    w = w_crud.create(word, meaning)
    return jsonify(w.__to_dict__())


@app.post('/learn')
async def learn():
    word_ids = request.json['word_ids']
    words = []
    for id in word_ids:
        word = w_crud.read(id)
        if word:
            words.append(word)
    tabs = t_crud.get_all_tabs()
    rendered_html = render_template('learn.html', words=words, tabs=tabs)
    return rendered_html


if __name__ == '__main__':
    app.run(
        host='localhost',
        port=8000
    )
