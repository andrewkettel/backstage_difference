from ninja import ModelSchema, Schema

from .models import OccurenceCount


class DifferenceOutputSchema(ModelSchema):
    class Meta:
        model = OccurenceCount
        fields = "datetime", "value", "number", "occurences", "last_datetime"


class Error(Schema):
    message: str
