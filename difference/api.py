from math import pow

from ninja import NinjaAPI, Router

from difference.schema import DifferenceOutputSchema, Error

api = NinjaAPI()
router = Router()


@router.get("/difference", response={200: DifferenceOutputSchema, 422: Error})
def difference(request, number: int):
    if number > 100:
        return 422, {"message": "Value for 'number' too large, must be <=100"}

    sum_of_squares = 0
    sum_of_number = 0
    for i in range(1, number + 1):
        sum_of_squares += pow(i, 2)
        sum_of_number += i
    square_of_sum = pow(sum_of_number, 2)
    difference = abs(sum_of_squares - square_of_sum)

    return {"value": difference, "number": number}


api.add_router("", router)
