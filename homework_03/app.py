from fastapi import FastAPI

application = FastAPI()

@application.get("/ping/")
def ping_answer():
    return {"message": "pong"}