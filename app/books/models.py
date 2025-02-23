import uuid
from dataclasses import dataclass, field


@dataclass
class Book:
    id: str = field(default=str(uuid.uuid4()))
    title: str = field(default='', metadata={'required': True})
    author: str = field(default='', metadata={'required': True})
    year: int = field(default=0, metadata={'required': True})


books = [
    Book(
        str(uuid.uuid4()),
        title='Book 1',
        author='Author 1',
        year=2020,
    ),
    Book(
        str(uuid.uuid4()),
        title='Book 2',
        author='Author 2',
        year=2022,
    ),
    Book(
        str(uuid.uuid4()),
        title='Book 3',
        author='Author 3',
        year=2023,
    )
]
