from datetime import datetime
from django.utils import timezone

from ninja import NinjaAPI, Router

from difference.models import OccurenceCount
from difference.schema import DifferenceOutputSchema, Error


router = Router()


@router.get("/difference", response={200: DifferenceOutputSchema, 422: Error})
def difference(request, number: int):
    # validate that number is less than 100
    if number > 100:
        return 422, {"message": "Value for 'number' too large, must be <= 100"}
    if number <= 0:
        return 422, {"message": "Value for 'number' too small, must be > 0"}

    # Get, update, store occurance count
    occ_count, created = OccurenceCount.objects.get_or_create(number=number)
    if not created:
        occ_count.last_datetime = occ_count.datetime
        occ_count.occurences += 1
        occ_count.save()
    else:
        # First time seeing this number, calculate the difference
        sum_of_squares: int = 0
        sum_of_number: int = 0
        for i in range(1, number + 1):
            sum_of_squares += i * i
            sum_of_number += i
        square_of_sum = sum_of_number * sum_of_number

        occ_count.number = number
        occ_count.value = abs(sum_of_squares - square_of_sum)
        occ_count.occurences += 1
        occ_count.save(update_fields=["number", "value", "occurences"])

    return occ_count
