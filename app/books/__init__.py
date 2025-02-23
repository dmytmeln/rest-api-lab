from flask import Blueprint

book_bp = Blueprint(
    'books',
    __name__,
    url_prefix='/api/v1/books'
)

from . import views
