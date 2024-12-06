from fastapi import FastAPI

app = FastAPI()



worlds = {
    "world1": {"w": "1"},
    "world2": {"w": "2"}
}

@app.get("/world/{name}")
# async def first_api():
#     return {"message": "Hi!!"}

async def world(name: int):
    return {"name": name}