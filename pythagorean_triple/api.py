from ninja import Router

from .schema import PythagoreanInputSchema, PythagoreanOutputSchema, Error

router = Router()


@router.post("/pythagorean_triple", response={200: PythagoreanOutputSchema, 422: Error})
def pythagorean_triple(request, input: PythagoreanInputSchema):
    return 422, {"message": "Not Implemented"}
