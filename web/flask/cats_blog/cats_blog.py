from flask import Flask

app = Flask(__name__)


@app.route('/')
def show_index():
    return "Index Page!"


@app.route('/blog')
def show_cats_blog():
    return "Cats blog!"


@app.route('/cats/<name>')
def show_cat(name):
    """Shows the cat page with the given name."""
    return "Cat - {}".format(name)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    """Shows the post with the given id."""
    return 'Post - {}'.format(post_id)


if __name__ == '__main__':
    app.run()
