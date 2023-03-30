from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class Items(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, null=True)
    harga = fields.FloatField(null=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)


Item_Pydantic = pydantic_model_creator(Items, name="Item")
ItemIn_Pydantic = pydantic_model_creator(Items, name="ItemIn", exclude_readonly=True)