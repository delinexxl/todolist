from sqlalchemy.orm import  Session
from app.repositories.category import CategoryREPOSITORY
from app.schemas.category import CategoryUpdateSchema,Categoryschema,Category_create


class CategoryNotFound(Exception):
    pass


class CategoryService:
    def __init__(self,db:Session)->None:
        self.db=db
        self.category_repository=CategoryREPOSITORY(db)

    def list_category(self)->list[Categoryschema]:
        category_orm=self.category_repository.get_all()
        return [Categoryschema.model_validate(categorys) for categorys in category_orm]


    def category_create(self,category_create:Category_create)->Categoryschema:
        category_orm = self.category_repository.create(name=category_create.name)
        self.db.commit()
        return Categoryschema.model_validate(category_orm)
    
    def category_update(self,category_id:str, update_category:CategoryUpdateSchema)->Categoryschema:
        category_to_update=self.category_repository.get_by_id(category_id=category_id)
        if not category_to_update:
            raise CategoryNotFound()

        if update_category.name is not None:
            category_to_update.name=update_category.name

        self.db.commit()
        return Categoryschema.model_validate(category_to_update)

    def category_delete(self,category_id:str)->Categoryschema:

        category_to_delete=self.category_repository.get_by_id(category_id=category_id)
        if not category_to_delete:
            raise CategoryNotFound()

        self.category_repository.delete(category_to_delete)
        self.db.commit()
