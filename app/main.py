from fastapi import FastAPI

app = FastAPI()


@app.get("/health-check")
def read_root():
    return {"msg": "Server is healthy!"}