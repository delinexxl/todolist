from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import APIRouter,Depends,status,HTTPException

from app.schemas.category import Categoryschema,CategoryUpdateSchema,Category_create
from app.services.category import CategoryService,CategoryNotFound
from app.api.dependencies import get_category_service
from app.schemas.category import CategoryUpdateSchema, Category_create, Categoryschema
from app.services.category import CategoryNotFound, CategoryService


router = APIRouter(prefix="/categories")

router=APIRouter(prefix='/categories')


@router.get('')
def read_categories(category_service:CategoryService=Depends(get_category_service)) -> list[Categoryschema]:
    return category_service.list_category()



@router.post('',status_code=status.HTTP_201_CREATED)
def create_category(payload:Category_create,category_service:CategoryService=Depends(get_category_service))->Categoryschema:
    return category_service.category_create(category_create=payload)



@router.patch('/{category_id}')
def update_category(category_id:str, payload:CategoryUpdateSchema,category_service:CategoryService=Depends(get_category_service))->Categoryschema:
    try:
        return category_service.category_update(
            category_id=category_id,
            update_category=payload,
        )
        return category_service.category_update(category_id=category_id,update_category=payload)
    except CategoryNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)



@router.delete('/{category_id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id:str,category_service:CategoryService=Depends(get_category_service))->None:
    try:
        return category_service.category_delete(category_id=category_id)
    except CategoryNotFound:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)