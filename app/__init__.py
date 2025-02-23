from flask import Blueprint, Flask

from .books.views import handle_not_found, handle_bad_request

main_bp = Blueprint(
    'main',
    __name__,
    url_prefix='/api/v1'
)

from . import views


def create_app():
    app = Flask(__name__)
    from app.books import book_bp
    app.register_blueprint(book_bp)
    app.register_blueprint(main_bp)
    app.register_error_handler(404, handle_not_found)
    app.register_error_handler(400, handle_bad_request)
    return app
