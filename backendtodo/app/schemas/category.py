from pydantic import BaseModel,ConfigDict




class Categoryschema(BaseModel):
    model_config=ConfigDict(from_attributes=True)
    id:str
    name:str
class Category_create(BaseModel):
    name:str
class CategoryUpdateSchema(BaseModel):
    name:str | None=None
