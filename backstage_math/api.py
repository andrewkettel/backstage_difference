from ninja import NinjaAPI

from difference.api import router as difference_router
from pythagorean_triple.api import router as pythagorean_router

api = NinjaAPI()

api.add_router("", difference_router)
api.add_router("", pythagorean_router)
