import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev', DATABASE=os.path.join(app.instance_path, 'cats_blog.sqlite'))

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

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

    return app


if __name__ == '__main__':
    create_app().run()
