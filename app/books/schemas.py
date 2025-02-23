from marshmallow import Schema, fields
from marshmallow.validate import Length, Range


class BookSchema(Schema):
    id = fields.Str(dump_only=True)
    title = fields.Str(required=True, validate=Length(min=2, max=100))
    author = fields.Str(required=True, validate=Length(min=2, max=50))
    year = fields.Int(required=True, validate=Range(min=1, max=2025))


book_schema = BookSchema()
books_schema = BookSchema(many=True)