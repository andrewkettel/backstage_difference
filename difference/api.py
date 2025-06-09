from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/difference")
def difference(request):
    return "nothing yet"
