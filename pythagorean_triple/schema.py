from ninja import Schema


class PythagoreanInputSchema(Schema):
    a: int
    b: int
    c: int


class PythagoreanOutputSchema(Schema):
    is_triple: bool
    product: int


class Error(Schema):
    message: str
