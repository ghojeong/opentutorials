from flask import Flask
from random import random

app = Flask(__name__)

topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]

def liTags():
    return "".join(
        map(lambda topic: f"<li><a href='/read/{topic['id']}'>{topic['title']}</a></li>"
            , topics)
    )

def template(contents, content="Welcome"):
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>{contents}</ol>
            <h2>{content}</h2>
        </body>
    </html>
    '''

@app.route("/")
def index():
    return template(liTags())

@app.route("/create")
def create():
    return "Create"

@app.route("/read/<int:id>", methods=["GET"])
def read(id):
    content = 'Welcome'
    for topic in topics:
        if id == topic['id']:
            content = topic['body']
    return template(liTags(), content)

app.run(port=5000, debug=True)
