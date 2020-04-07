import pybreaker as pybreaker
from circuitbreaker import circuit

from fastapi import FastAPI
from starlette.responses import RedirectResponse, PlainTextResponse

app = FastAPI(
    title="Client application",
    description="This is the application which makes request to a microservice.",
    version="2.5.0",
)

@app.get("/")
async def root():
    return {"message": "Client Application"}

@circuit(failure_threshold=2, expected_exception=ConnectionError)
@app.get("/redirect")
async def redirect():
 return RedirectResponse("http://127.0.0.1:8080/users")


