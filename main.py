from fastapi import FastAPI
import uvicorn

app = FastAPI()

counters = {}


@app.get('/')
def main():
    return "7632"


uvicorn.run(app)