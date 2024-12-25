from fastapi import APIRouter,Depends,status,HTTPException
import schemas,database,models
from sqlalchemy.orm import Session
from hashing import Hash
from mytoken import create_access_token
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
router=APIRouter(
    tags=['authentication']
)
@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    librarian=db.query(models.Librarians).filter(models.Librarians.email==request.username).first()
    #we are checking the user
    if not librarian:
        #if user is not available
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Invalid credentials')
    if not Hash.verify(librarian.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Incorrect password')
    #generate a JWT token and return
 
    #if everything is fine then we are passing the email to toekn
  
    access_token= create_access_token(data={"sub":librarian.email})
    return {"access_token":access_token,"token_type":"bearer"}
