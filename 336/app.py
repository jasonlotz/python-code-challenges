from fastapi import FastAPI

app = app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to PyBites' FastAPI Learning Path 🐍 🎉"}
