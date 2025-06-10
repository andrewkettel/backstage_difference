from ninja import Router

from difference.models import OccurenceCount
from difference.schema import DifferenceOutputSchema, Error
from difference.utils import calculate_difference


router = Router()


@router.get("/difference", response={200: DifferenceOutputSchema, 422: Error})
def difference(request, number: int):
    # validate that number is less than 100
    if number > 100:
        return 422, {"message": "Value for 'number' too large, must be <= 100"}
    if number <= 0:
        return 422, {"message": "Value for 'number' too small, must be > 0"}

    # Get, update, store occurance count
    occ_count, created = OccurenceCount.objects.get_or_create(
        number=number,
        defaults={"occurences": 1},
    )
    if not created:
        occ_count.last_datetime = occ_count.datetime
        occ_count.occurences += 1
        occ_count.save(update_fields=["occurences", "last_datetime", "datetime"])
    else:
        # First time seeing this number, calculate the difference
        # Set stored solution for quicker lookup
        occ_count.value = calculate_difference(number)
        occ_count.save(update_fields=["value"])

    return occ_count
