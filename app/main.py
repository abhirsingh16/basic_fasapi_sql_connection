from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.crud.crud import search_inputs
from app.database.database import SessionLocal
from app.models.tablemap import masterinput  #SQLAlchemy Model
from app.schemas.schemas import MasterInputBase  #Pydentic Model
from typing import List, Optional
from sqlalchemy import or_

# Initialize the Application
app = FastAPI()

#Welcome Message
@app.get("/")
def welcome():
    return {'message: Welcome'}

# Dependecies to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/records/", response_model=MasterInputBase)
# Create a new record
def create_record(record: MasterInputBase, db: Session = Depends(get_db)):
    db_record = masterinput(**record.model_dump())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record   # Returning sqlalchemy model, FastAPI will convert it to Pydantic model automatically



# Search for records
@app.get("/search_inputs/", response_model = List[MasterInputBase])
def search_inputs(
    q:Optional[str]=Query(None, description="Search query to filter records"),
    db: Session = Depends(get_db)
):
    if not q:
        raise HTTPException(status_code = 404, detail= "Search query parameter 'q' is required")
    

    query = db.query(masterinput).filter(
        or_(
            masterinput.category.ilike(f"%{q}%"),
            masterinput.city.ilike(f"%{q}%"),
            masterinput.name.ilike(f"%{q}%"),
            masterinput.area.ilike(f"%{q}%"),
            masterinput.address.ilike(f"%{q}%"),
            masterinput.phone_no_1.ilike(f"%{q}%"),
            masterinput.phone_no_2.ilike(f"%{q}%"),
            masterinput.url.ilike(f"%{q}%"),
            masterinput.ratings.ilike(f"%{q}%"),
            masterinput.extra_column3_type_of_products.ilike(f"%{q}%"),
            masterinput.extra_column10_type_of_course.ilike(f"%{q}%"),
            masterinput.sub_category.ilike(f"%{q}%"),
            masterinput.state.ilike(f"%{q}%"),
            masterinput.country.ilike(f"%{q}%"),
            masterinput.extra_column6_Source_File.ilike(f"%{q}%"),
            masterinput.extra_column1_ifsc.ilike(f"%{q}%"),
            masterinput.extra_column5_micr.ilike(f"%{q}%"),
            masterinput.extra_column9_branch_code.ilike(f"%{q}%"),
            masterinput.extra_column7_branch.ilike(f"%{q}%"),
            masterinput.extra_column8_Address.ilike(f"%{q}%"),
            masterinput.extra_column2_district.ilike(f"%{q}%"),
            masterinput.email.ilike(f"%{q}%"),
            masterinput.extra_column4_avg_fees.ilike(f"%{q}%"),
            masterinput.latitude.ilike(f"%{q}%"),
            masterinput.longitude.ilike(f"%{q}%"),
            masterinput.reviews.ilike(f"%{q}%"),
            masterinput.facebook_url.ilike(f"%{q}%"),
            masterinput.linkedin_url.ilike(f"%{q}%"),
            masterinput.twitter_url.ilike(f"%{q}%"),
            masterinput.description.ilike(f"%{q}%"),
            masterinput.pincode.ilike(f"%{q}%"),
            masterinput.virtual_phone_no.ilike(f"%{q}%"),
            masterinput.whatsapp_no.ilike(f"%{q}%"),
            masterinput.phone_no_3.ilike(f"%{q}%"),
            masterinput.avg_spent.ilike(f"%{q}%"),
            masterinput.cost_for_two.ilike(f"%{q}%"),  
        )
    )
    
    results = query.all()
    if not results:
        raise HTTPException(status_code=404, detail="No matching records found")
    return results