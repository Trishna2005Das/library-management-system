from fastapi import APIRouter,Depends,status,HTTPException
from typing import List
import schemas,database,models
from sqlalchemy.orm import Session
# from hashing import Hash


def get_issues(db:Session):
    issue_list=db.query(models.Issues).all()
    return issue_list

def add_issue(request: schemas.IssueBase, db: Session):
    new_issue = models.Issue(
        Issue_ID=request.Issue_ID,
        Student_ID=request.Student_ID,
        Book_ID=request.Book_ID,
        IssueDate=request.IssueDate,
        DueDate=request.DueDate,
        ReturnDate=request.ReturnDate
    )
    db.add(new_issue)
    db.commit()
    db.refresh(new_issue)
    return new_issue

def update_issue(id:int, request: schemas.IssueBase, db: Session):
    issue = db.query(models.Issues).filter(models.Issues.Issue_ID == id)
    if not issue.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Issue with id: {id} does not exist")
    issue.update(request.dict())
    db.commit()
    return issue

def delete_issue(id:int,db:Session):
    issue=db.query(models.Issues).filter(models.Issues.Issue_ID==id)
    if not issue.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'issue with id {id} is not available')
    issue.delete(synchronize_session=False)
    db.commit()
    return 'done'

