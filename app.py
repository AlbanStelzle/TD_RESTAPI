from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pymongo import MongoClient
from model_egg import ModelEgg

app = FastAPI()
client = MongoClient('mongodb')
# Accès à la base de données "eggs_database"
db = client["eggs_database"]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/eggs')
async def eggs():
    eggs = db.eggs.find()
    result = []
    for egg in eggs:
        result.append(egg)
    return result


@app.get('/eggs/{egg_immat}')
async def eggs(egg_immat):
    egg = db.eggs.find_one({"immatriculation": egg_immat})
    return egg


@app.post('/eggs')
async def eggs(egg: ModelEgg):
    existing_egg = await db.eggs.find_one({"immatriculation": egg.immatriculation})
    print(existing_egg)
    if existing_egg is not None:
        raise HTTPException(status_code=400, detail="Egg with this immatriculation already exists")
    try:
        db.eggs.insert_one(egg.dict())
        return {"message": "Egg added"}
    except Exception as e:
        return HTTPException(status_code=400, detail="Egg already exists")


@app.delete("/eggs/{immatriculation}")
async def delete_egg(immatriculation: str):
    result = await db.eggs.delete_one({"immatriculation": immatriculation})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Egg not found")
    return {"result": "egg deleted"}


@app.put("/eggs/{immatriculation}")
async def update_egg(immatriculation: str, egg: ModelEgg):
    existing_egg = await db.eggs.find_one({"immatriculation": immatriculation})
    if existing_egg is None:
        raise HTTPException(status_code=404, detail="Egg not found")

    result = await db.eggs.update_one(
        {"immatriculation": immatriculation},
        {"$set": egg.dict()}
    )

    if result.modified_count == 0:
        raise HTTPException(status_code=400, detail="No changes made to the egg")
    return {"result": "egg updated"}
