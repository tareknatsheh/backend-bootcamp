from fastapi import FastAPI
from routes import students, auth

"""
TODO
- Create routes V
- Put db code (json read/write) in another folder V
- Add Authentication using jwt
- raise exceptions
- handle edge cases
- write tests
- create a README.md
"""

app = FastAPI()

app.include_router(students.router)
app.include_router(auth.router)


@app.get("/")
def home():
    return "Welcome to School API"


