from app.models.tablemap import masterinput  #SQLAlchemy Model
from sqlalchemy import or_
from sqlalchemy.orm import Session
from app.schemas.schemas import MasterInputBase
from fastapi import Depends
# from app.main import get_db




def search_inputs(db: Session, q: str, skip: int = 0, limit: int = 10):
    """
    Search across multiple columns for a given query.
    """
    search_columns = [
        masterinput.category,
        masterinput.city,
        masterinput.name,
        masterinput.area,
        masterinput.address,
        masterinput.phone_no_1,
        masterinput.phone_no_2,
        masterinput.url,
        masterinput.ratings,
        masterinput.extra_column3_type_of_products,
        masterinput.extra_column10_type_of_course,
        masterinput.sub_category,
        masterinput.state,
        masterinput.country,
        masterinput.extra_column6_Source_File,
        masterinput.extra_column1_ifsc,
        masterinput.extra_column5_micr,
        masterinput.extra_column9_branch_code,
        masterinput.extra_column7_branch,
        masterinput.extra_column8_Address,
        masterinput.extra_column2_district,
        masterinput.email,
        masterinput.extra_column4_avg_fees,
        masterinput.latitude,
        masterinput.longitude,
        masterinput.reviews,
        masterinput.facebook_url,
        masterinput.linkedin_url,
        masterinput.twitter_url,
        masterinput.description,
        masterinput.pincode,
        masterinput.virtual_phone_no,
        masterinput.whatsapp_no,
        masterinput.phone_no_3,
        masterinput.avg_spent,
        masterinput.cost_for_two
    ]

    # build a dynamic search query using 'or_'
    query = db.query(masterinput)

    if q:
        query = query.filter(
            or_(
                *[column.ilike(f"%{q}%") for column in search_columns]
            )
        )
    return query.offset(skip).limit(limit).all()
