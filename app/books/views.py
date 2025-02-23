from flask import jsonify, request, make_response, abort
from marshmallow import ValidationError

from app.books import book_bp
from app.books.models import books, Book
from app.books.schemas import books_schema, book_schema


def get_book_by_id(book_id):
    return next((b for b in books if b.id == book_id), None)


@book_bp.route('/', methods=['GET'])
def get_books():
    return make_response(jsonify(books_schema.dump(books)))


@book_bp.route('/<book_id>', methods=['GET'])
def get_book(book_id):
    book = get_book_by_id(book_id)
    return make_response(jsonify(book_schema.dump(book)), 200) if book else abort(404)


@book_bp.route('/', methods=['POST'])
def add_book():
    data = request.get_json()
    try:
        book = book_schema.load(data)
    except ValidationError as e:
        return make_response({'error': e.messages}, 400)
    book_to_add = Book(**book)
    books.append(book_to_add)
    return make_response(jsonify(book_schema.dump(book_to_add)), 201)


@book_bp.route('/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = get_book_by_id(book_id)
    if book:
        books.remove(book)
        return {}, 204
    return abort(404)


def handle_not_found(e):
    return {'error': 'Not found'}, 404


def handle_bad_request(e):
    return {'error': 'Bad request'}, 400
