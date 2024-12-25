from fastapi import APIRouter,Depends,status,HTTPException
from typing import List
import schemas,database,models,oauth2 #routers directory which is inside blog directory 
from sqlalchemy.orm import Session
from repository import issues
get_db=database.get_db
router=APIRouter(
    prefix="/Issues",
    tags=['Issues table'])



@router.get('/',response_model=List[schemas.ShowIssue])
def issue_all(db:Session=Depends(get_db)):
    return issues.get_issues(db)


@router.post('/', response_model=schemas.ShowIssue)
def add_issue(request: schemas.IssueBase, db: Session = Depends(get_db)):
    return issues.add_issue(request, db)

@router.put('/issues/{id}', response_model=schemas.ShowIssue)
def update_issue(id:int, request: schemas.IssueBase, db: Session = Depends(get_db)):
    return issues.update_issue(id, request, db)

@router.delete('/issues/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_issue(id:int, db: Session = Depends(get_db)):
    return issues.delete_issue(id, db)