from ninja import NinjaAPI

from difference.api import router as difference_router

api = NinjaAPI()

api.add_router("", difference_router)
