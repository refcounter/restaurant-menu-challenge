from fastapi import APIRouter

router = APIRouter(prefix='/pay', tags=['Pagamento'])

@router.post('/')
def pay():
    pass

