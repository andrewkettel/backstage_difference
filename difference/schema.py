from ninja import Schema


class DifferenceOutputSchema(Schema):
    number: int
    value: int


class Error(Schema):
    message: str
