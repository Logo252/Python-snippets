from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Index Page!"


@app.route('/blog')
def cats_blog():
    return "Cats blog!"


if __name__ == '__main__':
    app.run()
