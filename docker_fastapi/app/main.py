from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World this is my new API!"}

@app.get("/myname/{name}")
async def myName(name: str):
    return {"message": f"Hello {name} this is my new API!"}

@app.get("/technology")
async def redirect_typer():
    return RedirectResponse("https://images.pexels.com/photos/3978352/pexels-photo-3978352.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")