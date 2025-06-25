from fastapi import FastAPI
from handlers import routers
app = FastAPI()

for router in routers:
    app.include_router(router)
#
# class Person(BaseModel):
#     name: str | None = None
#     age: int = 1
#
# @app.get("/person",
#          description="This is the homepage",
#          summary="This is the homepage",
#          response_model=Person,
#          name="homepage")
# def get_person():
#     return Person(name="Alex", age='25')
#
#
# @app.post("/person", response_model=Person,
#           response_model_exclude_none=True)
# def create_person(person: Person):
#     return person