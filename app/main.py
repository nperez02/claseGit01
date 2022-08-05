from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World this is my new API!"}

@app.get("/myname/{name}")
async def myName(name: str):
    return {"message": f"Hello {name} this is my new API!"}