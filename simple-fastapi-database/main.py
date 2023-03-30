from fastapi import FastAPI
from models import Item_Pydantic, ItemIn_Pydantic, Items

from tortoise.contrib.fastapi import register_tortoise

app = FastAPI(title="Tortoise ORM FastAPI example")


@app.get("/items")
async def get_items():
    return await Item_Pydantic.from_queryset(Items.all())


@app.post("/items")
async def create_item(item: ItemIn_Pydantic):
    item_obj = await Items.create(**item.dict(exclude_unset=True))
    return await Item_Pydantic.from_tortoise_orm(item_obj)


register_tortoise(
    app,
    db_url="sqlite://:memory:",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)